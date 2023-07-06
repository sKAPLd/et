
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),
    path("registro", registro,name="registro"),
    path("subs", subs,name="subs"),
    path("catalogo", catalogo,name="catalogo"),
    path("carrito", carrito,name="carrito"),
    path("login", LoginView.as_view(template_name='core/login.html'), name="login"),
    path("logout", logout,name="logout"),
    path("addtocar/<codigo>", addtocar,name="addtocar"),
    path("limpiar", limpiar),
    path("dropitem/<codigo>", dropitem,name="dropitem"),
    path("comprar", comprar,name="comprar"),
    path("contacto", contacto,name="contacto"),
    path("historial", historial,name="historial"),
    path("adminproducto", adminproducto,name="adminproducto"),
    path("adminC", adminC,name="adminC"),
    path("suscribirme", suscribirme,name="suscribirme"),
    path("nosotros", nosotros,name="nosotros"),


















]
