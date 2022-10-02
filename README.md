
How to install Addresses into your project
-----------

1. Add "addresses" to your INSTALLED_APPS setting like this::
    ``` python
    INSTALLED_APPS = [
        'addresses',
    ]
    ```

2. You can then create a model relationship to addresses like this:
    ```python
   from django.db import models
   from addresses.models import Address

   class Suppliers(models.Model):
       ...
       addresses = GenericRelation(Address, related_query_name="suppliers")


Releasing
---------

1. Increment version number in setup.cfg

2. Commit and push changes.

3. Create release on GitHub with the version number

4. The release can then be installed into Django projects like this:
    ```
    git+ssh://git@github.com/Natoora/Addresses.git@{version number} (Leave "@{version number} out for latest version)
   ```
