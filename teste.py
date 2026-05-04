from gestao.models import Imoveis

imoveis = Imoveis.objects.all()
print(imoveis)