Installation
============

Install using pip:

.. code-block:: sh

    pip install gargoyle-yplan

If you are upgrading from the original to this fork, you will need to run the following first, since the packages
clash:

.. code-block:: bash

    pip uninstall django-modeldict gargoyle

Failing to do this will mean that ``pip uninstall gargoyle`` will also erase the files for `gargoyle-yplan`, and
similarly for our `django-modeldict` fork.

Enable Gargoyle
---------------

Once you've downloaded the Gargoyle package, you simply need to add it to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'gargoyle',
    )

*If you do not use Nexus*, you will also need to enable discovery of ``gargoyle.py`` modules (which contain
``ConditionSet``\s). The best place to do this is within your ``urls.py`` file:

.. code-block:: python

    import gargoyle

    gargoyle.autodiscover()

If you do use ``gargoyle.py`` files, Python 2.7, and the autodiscovery code, you'll need to ensure your imports are not
relative:

.. code-block:: python

    from __future__ import absolute_import

    from gargoyle.conditions import ConditionSet

Nexus Frontend
--------------

While Gargoyle can be used without a frontend, we highly recommend using `Nexus
<https://github.com/YPlan/nexus-yplan>`_.

Nexus will automatically detect Gargoyle's ``NexusModule``, assuming its autodiscovery is on. If not, you will need to
register the module by hand:

.. code-block:: python

    from gargoyle.nexus_modules import GargoyleModule

    nexus.site.register(GargoyleModule, 'gargoyle')

Disabling Auto Creation
-----------------------

Under some conditions you may not want Gargoyle to automatically create switches that don't currently exist. To disable
this behavior, you may use the ``GARGOYLE_AUTO_CREATE`` setting your ``settings.py``:

.. code-block:: python

    GARGOYLE_AUTO_CREATE = False

Default Switch States
~~~~~~~~~~~~~~~~~~~~~

The ``GARGOYLE_SWITCH_DEFAULTS`` setting allows engineers to set the default state of a switch before it's been added
via the gargoyle admin interface. In your ``settings.py`` add something like:

.. code-block:: python

    GARGOYLE_SWITCH_DEFAULTS = {
        'new_switch': {
          'is_active': True,
          'label': 'New Switch',
          'description': 'When you want the newness',
        },
        'funky_switch': {
          'is_active': False,
          'label': 'Funky Switch',
          'description': 'Controls the funkiness.',
        },
    }
