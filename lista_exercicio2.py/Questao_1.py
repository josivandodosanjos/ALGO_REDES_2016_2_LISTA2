cont_reg = 0
cont_bom = 0
cont_oti = 0

for i in range(10):
    opiniao = int(input('Digite sua opiniao sobre o filme: '))

    if opiniao == 1:
        cont_reg = cont_reg + 1
    elif opiniao == 2:
        cont_bom = cont_bom + 1
    else:
        cont_oti = cont_oti + 1

print('Qtd de opiniao em REGULAR = %d' % cont_reg)
print('Qtd de opiniao em BOM = %d' % cont_bom)
print('Qtd de opiniao em OTIMO = %d' % cont_oti)

