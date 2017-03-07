import webapp

class redirect(webapp.webApp):
    def process(self, parsedREquest):
        import random
        numero = random.randint(1,100000000)
        return ("303 See Other", "<html><body><a href= '"+
                str(numero)+"'>Clic aqui para redirigirte</a></body></html>")


#        return ("303 See Other", "<html><head><meta http-equiv='Refresh' " +
#                        "content='5;url=" + str(randomURL) + "'></head>" +
#                        "<body><p>Seras redireccionado en 5 segundos o si haces click " +
#                        "<a href='" + str(randomURL) + "'>aqui</a></p></body></html>")

if __name__ == "__main__":
    testRedirecting = redirect("localhost", 1234)
