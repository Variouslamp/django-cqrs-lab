from django.shortcuts import render

# -----------------------------------------------------------------------------
# Define a que pagina se redirige el usuario respecto a su eleccion de rol


def index(request):
    return render(request, "roles/select_role.html")


# -----------------------------------------------------------------------------
