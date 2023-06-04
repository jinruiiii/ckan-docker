import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.extrafields.cli as cli
# import ckanext.extrafields.helpers as helpers
# import ckanext.extrafields.views as views
# from ckanext.extrafields.logic import (
#     action, auth, validators
# )


class ExtrafieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    
    # # plugins.implements(plugins.IAuthFunctions)
    # # plugins.implements(plugins.IActions)
    # # plugins.implements(plugins.IBlueprint)
    # # plugins.implements(plugins.IClick)
    # # plugins.implements(plugins.ITemplateHelpers)
    # # plugins.implements(plugins.IValidators)
    
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "extrafields")
        
    # IDatasetForm  
    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(ExtrafieldsPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            'who': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]
        })
        schema.update({
            'what': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]
        })
        return schema
   
    def update_package_schema(self):
        schema = super(ExtrafieldsPlugin, self).update_package_schema()
        # our custom field
        schema.update({
            'who': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]
        })
        schema.update({
            'what': [toolkit.get_validator('ignore_missing'),
                            toolkit.get_converter('convert_to_extras')]
        })
        return schema
    
    def show_package_schema(self):
        schema = super(ExtrafieldsPlugin, self).show_package_schema()
        schema.update({
            'who': [toolkit.get_converter('convert_from_extras'),
                            toolkit.get_validator('ignore_missing')]
        })
        schema.update({
            'what': [toolkit.get_converter('convert_from_extras'),
                            toolkit.get_validator('ignore_missing')]
        })
        return schema   
    
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return [] 
    
    
    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
