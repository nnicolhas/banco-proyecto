from ninja import Router

public_router = Router(tags=["Catálogos"])

@public_router.get("/technologies")
def list_technologies(request):
    return []