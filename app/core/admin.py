from django.contrib import admin
from cloudinary.forms import CloudinaryFileField
from cloudinary import uploader
from cloudinary.exceptions import Error
from django.db import models

from .models import Post, Tag


def delete_image(public_id):
    try:
        uploader.destroy(public_id)
        print(f"Image with public ID '{public_id}' deleted successfully.")
    except Error as e:
        print(f"Error deleting image with public ID '{public_id}': {str(e)}")


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': CloudinaryFileField}
    }

    def save_model(self, request, obj, form, change):
        if change and 'image' in form.changed_data:
            # Save the new image to Cloudinary
            result = uploader.upload(obj.image)

            # Delete the old image if it exists
            existing_obj = Post.objects.get(pk=obj.pk)
            if existing_obj.image and hasattr(existing_obj.image, 'public_id'):
                public_id = existing_obj.image.public_id
                uploader.destroy(public_id)

            # Update the image field with the new secure URL
            obj.image = result.get('secure_url', '')

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Delete associated image from Cloudinary
        if obj.image:
            public_id = obj.image.public_id
            delete_image(public_id)

        # Call the default delete_model method to delete the object
        super().delete_model(request, obj)


admin.site.register(Post, MyModelAdmin)
admin.site.register(Tag)
