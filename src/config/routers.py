class CQRSRouter:
    def db_for_read(self, model, **hints):
        # Todo lo que venga de la app de lectura va a la DB de lectura
        if model._meta.app_label == 'product_view_app':
            return 'query'
        return 'default'

    def db_for_write(self, model, **hints):
        # Todo lo que sea escribir (Commands) va a la DB principal
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return 'default'
