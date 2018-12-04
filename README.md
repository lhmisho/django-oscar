# django-oscar
A light weight eCommerce site build with django-oscar

# step 1:
after installtion if product image is not show than have to uninstall pillow than install 'libjpeg-dev' than need to install pilllow again

```python
pip uninstall pillow
apt-get install libjpeg-dev # or whatever similar in your server
pip install pillow # yes again
```
# step 2:
add this to urls.py
-------------------

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```
