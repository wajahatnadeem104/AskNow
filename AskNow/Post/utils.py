def post_image_location(instance, filename):
    file_path = 'post_media/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.username),
        title=str(instance.title),
        filename=filename
    )
    return file_path
