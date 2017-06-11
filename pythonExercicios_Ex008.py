#converter M em cm e mm
m = float (input('Digite o número em métros: '))
cm = m*100
mm = m*1000
print('Em metros {} em Centímetos {:.0f} e em Milímetros {:.0f}'.format(m, cm, mm))
