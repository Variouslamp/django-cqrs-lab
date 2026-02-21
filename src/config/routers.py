class CQRSRouter:
    def db_for_read(self, model, **hints):
        # Todo lo que venga de la app de lectura va a la DB de lectura
        if model._meta.app_label == 'queries_app':
            return 'query'
        return 'command'

    def db_for_write(self, model, **hints):
        # Todo lo que sea escribir (Commands) va a la DB principal
        return 'command'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Esto es vital para no crear tablas innecesarias en la nube
        if app_label == 'queries_app':
            return db == 'query'
        elif app_label == 'commands_app':
            return db == 'command'
        return None
