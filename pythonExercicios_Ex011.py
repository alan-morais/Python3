#medir m² e quantidade de tinta
alt = float(input('Digite a altura: '))
com = float(input('Digite o comprimento: '))
mq = alt*com
tinta = (mq/2)
print('Sua parede tem {} m² e você pode usar até {}l de tinta'.format(mq, tinta))
