# -*- coding: utf-8 -*-

#--- Definiciones y opciones ---
def_tipo_valor = {
	'01': 'Cartera total',
	'02': 'Cartera vigente',
	'03': 'Cartera vencida',
	'04': 'Número de créditos',
	'05': 'Número de acreditados',
	'21': 'Tasa de interés MN',
	'22': 'Tasa de interés ME',
	'23': 'Tasa de interés UDIS',
	'51': 'Plazo ponderado en meses (remanente)'
}

cat_variables = {
	'01': 'saldo_total',
	'02': 'car_vigente',
	'03': 'car_vencida',
	'04': 'creditos',
	'05': 'acreditados',	
	'21': 'tasa_i_mn',
	'22': 'tasa_i_me',
	'23': 'tasa_i_udis',
	'51': 'plazo_ponderado'
}

def_variables  = {
	'saldo_total': 'Monto dispuesto'.decode('utf-8'),
	'car_vigente': 'Cartera vigente'.decode('utf-8'),
	'car_vencida': 'Cartera vencida'.decode('utf-8'),
	'creditos': 'Número de créditos'.decode('utf-8'),
	'acreditados': 'Número de acreditados'.decode('utf-8'),
	'tasa_i_mn': 'Tasa de interés MN'.decode('utf-8'),
	'tasa_i_me': 'Tasa de interés ME'.decode('utf-8'),
	'tasa_i_udis': 'Tasa de interés UDIS'.decode('utf-8'),
	'plazo_ponderado': 'Plazo ponderado en meses (remanente)'.decode('utf-8'),
	'concentracion_cartera': 'Concentración de cartera por cliente'.decode('utf-8'),
	'saldo_acum': 'Saldo acumulado por cliente'.decode('utf-8'),
	'porc_acum': 'Saldo acumulado por cliente'.decode('utf-8'),
	'tasa': 'Tasa de interés ponderada'.decode('utf-8'),
	'plazo': 'Plazo ponderado (remanente)'.decode('utf-8'),
	'imor': 'Índice de Morosidad (IMOR)'.decode('utf-8')
}


def_variables_lead = {
	'total':{
		'saldo_total': 'Saldo total'.decode('utf-8'),				
		'creditos': 'Número de créditos totales'.decode('utf-8'),
		'acreditados': 'Número de acreditados totales'.decode('utf-8'),	
		'concentracion_cartera': 'Concentración de cartera por cliente del portafolio total'.decode('utf-8'),
		'saldo_acum': 'Saldo acumulado por cliente del portafolio total'.decode('utf-8'),
		'porc_acum': 'Saldo acumulado por cliente del portafolio total'.decode('utf-8'),
		'tasa': 'Tasa de interes ponderada del portafolio total'.decode('utf-8'),
		'plazo': 'Plazo ponderado de los creditos remanentes'.decode('utf-8'),
		'imor': 'Índice de Morosidad del portafolio total'.decode('utf-8')
	},

	'marginal':{
		'saldo_total': 'Incremento marginal en monto dispuesto'.decode('utf-8'),
		'creditos': 'Incremento marginal en número de créditos emitidos'.decode('utf-8'),
		'acreditados': 'Incremento marginal en número de acreditados'.decode('utf-8'),				
		
		'tasa': 'Tasa de interes de nuevos créditos emitidos'.decode('utf-8'),
		'plazo': 'Plazo ponderado de los nuevos créditos emitidos'.decode('utf-8'),
	}
}

def_variables_unidades  = {
	'saldo_total': 'Pesos ($MXN)'.decode('utf-8'),
	'car_vigente': 'Pesos ($MXN)'.decode('utf-8'),
	'car_vencida': 'Pesos ($MXN)'.decode('utf-8'),
	'creditos': 'Creditos (Número)'.decode('utf-8'),
	'acreditados': 'Acreditados (Número)'.decode('utf-8'),
	'tasa_i_mn': 'Porcentaje (%)'.decode('utf-8'),
	'tasa_i_me': 'Porcentaje (%)'.decode('utf-8'),
	'tasa_i_udis': 'Porcentaje (%)'.decode('utf-8'),
	'plazo_ponderado': 'Meses (Número)'.decode('utf-8'),
	'concentracion_cartera': 'Concentración de cartera por cliente'.decode('utf-8'),
	'saldo_acum': 'Pesos ($MXN)'.decode('utf-8'),
	'porc_acum': 'Porcentaje (%)'.decode('utf-8'),
	'tasa': 'Porcentaje (%)'.decode('utf-8'),
	'plazo': 'Meses (Número)'.decode('utf-8'),
	'imor': 'Porcentaje (%) [Cartera Vencida/Cartera Total]'.decode('utf-8')
}

opc_variables = [
	'saldo_total',
	# 'car_vigente',
	# 'car_vencida',
	'creditos',
	'acreditados',
	'tasa',
	'plazo',
	'imor',
	# 'tasa_i_mn',
	# 'tasa_i_me',
	# 'tasa_i_udis',
	# 'plazo_ponderado',
	'concentracion_cartera'
]

def_cortes = {
	'periodo': 'Periodo'.decode('utf-8'),
	'institucion': 'Banco'.decode('utf-8'),
	'estado': 'Entidad Federativa'.decode('utf-8'),
	'tec': 'Tamaño de Empresa'.decode('utf-8'),
	'cliente': 'Cliente'.decode('utf-8'),
	'intervalo': 'Intervalo de Plazo'.decode('utf-8'),
	'monto': 'Monto del crédito [miles]'.decode('utf-8'),
	'moneda': 'Moneda'.decode('utf-8'),
	'destino': 'Destino del crédito'.decode('utf-8'),
	'garantia': 'Tipo de garantía'.decode('utf-8'),
	'calificacion': 'Calificación'.decode('utf-8'),
	'sector': 'Sector económico'.decode('utf-8')
}


opc_cortes = [
	'institucion',
	'periodo',
	'estado',
	'tec',
	'intervalo',
	'monto',
	'moneda',
	'destino',
	'garantia',
	'calificacion',
	'sector'
]

def_secciones = {
	'S99': 'Menu',
	'S00': 'General',
	'S01': 'Por tamaño de empresa',
	'S02': 'Por región geográfica',
	'S03': 'Efectividad de sucursales',
	'S04': 'Tasas y precios',
	'S05': 'Cartera vencida y riesgos',
	'S06': 'Por sector'
}

opc_secciones = [
	['S99', 'Menu'],
	['S00', 'General'],
	['S01', 'Por tamaño de empresa'],
	['S02', 'Por región geográfica'],
	['S03', 'Efectividad de sucursales'],
	['S04', 'Tasas y precios'],
	['S05', 'Cartera vencida y riesgos'],
	['S06', 'Por sector']
]

def_bulk_slide_import = {
	'Slide0.PNG': ['Menu', ['S99']],
	'Slide1.PNG': ['Evolución y distribución de la cartera', ['S00']],
	'Slide2.PNG': ['Crecimiento en originaciones', ['S00']],
	'Slide3.PNG': ['Componentes del portafolio (1/2)', ['S00']],
	'Slide4.PNG': ['Componentes del portafolio (2/2)', ['S00']],
	'Slide5.PNG': ['Crecimiento vs. portafolio total', ['S00']],
	'Slide6.PNG': ['Componentes del portafolio', ['S00']],
	'Slide7.PNG': ['Distribución de cartera por tamaño de empresa', ['S00', 'S01']],
	'Slide8.PNG': ['Distribución de cartera por sector económico', ['S00', 'S06']],
	'Slide9.PNG': ['Distribución de cartera por región geográfica', ['S00', 'S02']],
	'Slide10.PNG': ['FALTA (NO LA VAMOS A HACER)', []],
	'Slide11.PNG': ['Cartera por tamaño de empresa', ['S01']],
	'Slide12.PNG': ['Componentes del portafolio', ['S01']],
	'Slide13.PNG': ['Componentes del portafolio', ['S01']],
	'Slide14.PNG': ['Crecimiento vs. portafolio total', ['S01']],
	'Slide15.PNG': ['Distribución de créditos empresariales por tamaño de empresa', ['S01']],
	'Slide16.PNG': ['Cartera por región', ['S02']],
	'Slide17.PNG': ['Componentes del portafolio', ['S02']],
	'Slide18.PNG': ['Componentes del portafolio', ['S02']],
	'Slide19.PNG': ['Crecimiento vs. portafolio total (1/3)', ['S02']],
	'Slide20.PNG': ['Crecimiento vs. portafolio total (2/3)', ['S02']],
	'Slide21.PNG': ['Crecimiento vs. portafolio total (3/3)', ['S02']],
	'Slide22.PNG': ['Distribución de créditos empresariales por región geográfica', ['S02']],
	'Slide23.PNG': ['Existe una alta correlación entre la participación de sucursales con la participación de clientes y el share of wallet', ['S03']],
	'Slide24.PNG': ['Comparación de la efectividad por sucursal entre bancos', ['S03']],
	'Slide25.PNG': ['Efectividad sucursales por estado', ['S03']],
	'Slide26.PNG': ['Comparación de tasas de interés por tamaño de empresa', ['S04']],
	'Slide27.PNG': ['Comparación de tasas de interés por tamaño de crédito', ['S04']],
	'Slide28.PNG': ['Comparación de tasas de interés por calificación crediticia de la cartera', ['S04']],
	'Slide29.PNG': ['Comparación de la cartera vencida por tamaño de empresa', ['S05']],
	'Slide30.PNG': ['Comparación de la cartera vencida por tamaño de crédito', ['S05']],
	'Slide31.PNG': ['Correlación entre crecimiento en originaciones y tasa de interés promedio', ['S04']],
	'Slide32.PNG': ['Correlación entre crecimiento en originaciones y tasa de interés promedio por tamaño de empresa', ['S04']],
	'Slide33.PNG': ['Correlación entre riesgo (medido como cartera vencida) y tasa de interés promedio', ['S04', 'S05']],
	'Slide34.PNG': ['Correlación entre riesgo (medido como cartera vencida) y tasa de interés promedio por tamaño de empresa', ['S04', 'S05']],
	'Slide35.PNG': ['Correlación entre cartera total y tasa de interés promedio', ['S04']],
	'Slide36.PNG': ['Riesgo de concentración de clientes por banco', ['S05']],
	'Slide37.PNG': ['Cartera por sector', ['S06']],
	'Slide38.PNG': ['Componentes del portafolio por sector', ['S06']],
	'Slide39.PNG': ['Componentes del portafolio por sector', ['S06']],
	'Slide40.PNG': ['Crecimiento vs. portafolio total (1/3)', ['S06']],
	'Slide41.PNG': ['Crecimiento vs. portafolio total (2/3)', ['S06']],
	'Slide42.PNG': ['Crecimiento vs. portafolio total (3/3)', ['S06']],
	'Slide43.PNG': ['Distribución de créditos empresariales por sector económico', ['S06']],
	'Slide44.PNG': ['Evolución de la cartera vencida por banco', ['S05']],
	'Slide45.PNG': ['Evolución de la cartera vencida por tamaño de empresa y banco', ['S05']],
	'Slide46.PNG': ['FALTA (NO LA VAMOS A HACER)', []],
	

} 



def decode_options(options_list, corte):	
	result = []
	if corte == 'periodo':
		for opcion in options_list:
			result.append([int(opcion[0]), opcion[1].decode('utf-8')])
	else:	
		for opcion in options_list:
			result.append([opcion[0].decode('utf-8'), opcion[1].decode('utf-8')])
	return result


opc_tipo_valor = [
	['01', 'Cartera total'],
	['02', 'Cartera vigente'],
	['03', 'Cartera vencida'],
	['04', 'Número de créditos'],
	['05', 'Número de acreditados'],
	['21', 'Tasa de interés MN'],
	['22', 'Tasa de interés ME'],
	['23', 'Tasa de interés UDIS'],
	['51', 'Plazo ponderado en meses (remanente)']
]

def_institucion = {
	'00': 'Total Banca Múltiple',
	'11': 'ABC Capital',
	'12': 'Actinver',
	'13': 'Afirme',
	'14': 'American Express',
	'15': 'Autofin',
	'16': 'Banamex',
	'17': 'Banca Mifel',
	'18': 'Banco Ahorro Famsa',
	'19': 'Banco Azteca',
	'20': 'Banco Bancrea',
	'21': 'Banco Base',
	'22': 'Banco Bicentenario',
	'23': 'Banco Credit Suisse',
	'24': 'Banco del Bajío',
	'25': 'Banco Sabadell',
	'26': 'Banco Wal-Mart',
	'27': 'BanCoppel',
	'28': 'Bank of America',
	'29': 'Bank of Tokyo-Mitsubishi UFJ',
	'30': 'Bankaool',
	'31': 'Banorte/Ixe',
	'32': 'Banregio',
	'33': 'Bansí',
	'34': 'BBVA Bancomer',
	'35': 'CIBanco',
	'36': 'Consubanco',
	'37': 'Deutsche Bank',
	'38': 'Dondé Banco',
	'39': 'Finterra',
	'40': 'HSBC',
	'41': 'ICBC',
	'42': 'Inbursa',
	'43': 'ING',
	'44': 'Inmobiliario Mexicano',
	'45': 'Interacciones',
	'46': 'Intercam Banco',
	'47': 'Investa Bank',
	'48': 'Invex',
	'49': 'Ixe',
	'50': 'J.P. Morgan',
	'51': 'Monex',
	'52': 'Multiva',
	'53': 'Santander',
	'54': 'Santander Vivienda',
	'55': 'Scotiabank',
	'56': 'Ve por Más'
}

opc_institucion = [
	['00',  'Total Banca Múltiple'],
	
	['16',  'Banamex'],
	['31',  'Banorte/Ixe'],
	['34',  'BBVA Bancomer'],
	['40',  'HSBC'],
	['42',  'Inbursa'],
	['53',  'Santander'],
	['55',  'Scotiabank'],

	['11',  'ABC Capital'],
	['12',  'Actinver'],
	['13',  'Afirme'],
	['14',  'American Express'],
	['15',  'Autofin'],
	
	['17',  'Banca Mifel'],
	['18',  'Banco Ahorro Famsa'],
	['19',  'Banco Azteca'],
	['20',  'Banco Bancrea'],
	['21',  'Banco Base'],
	['22',  'Banco Bicentenario'],
	['23',  'Banco Credit Suisse'],
	['24',  'Banco del Bajío'],
	['25',  'Banco Sabadell'],
	['26',  'Banco Wal-Mart'],
	['27',  'BanCoppel'],
	['28',  'Bank of America'],
	['29',  'Bank of Tokyo-Mitsubishi UFJ'],
	['30',  'Bankaool'],
	
	['32',  'Banregio'],
	['33',  'Bansí'],
	
	['35',  'CIBanco'],
	['36',  'Consubanco'],
	['37',  'Deutsche Bank'],
	['38',  'Dondé Banco'],
	['39',  'Finterra'],
	
	['41',  'ICBC'],
	
	['43',  'ING'],
	['44',  'Inmobiliario Mexicano'],
	['45',  'Interacciones'],
	['46',  'Intercam Banco'],
	['47',  'Investa Bank'],
	['48',  'Invex'],
	['49',  'Ixe'],
	['50',  'J.P. Morgan'],
	['51',  'Monex'],
	['52',  'Multiva'],
	
	['54',  'Santander Vivienda'],
	
	['56',  'Ve por Más'],
]


def_tec = {
	'01': 'Micro',
	'02': 'Pequeña',
	'03': 'Mediana',
	'04': 'Grande',
	'05': 'Fideicomiso'
}


opc_tec = [
	['01',  'Micro'],
	['02',  'Pequeña'],
	['03',  'Mediana'],
	['04',  'Grande'],
	['05',  'Fideicomiso']
]


def_estado = {
	'01': 'Aguascalientes',
	'02': 'Baja California',
	'03': 'Baja California Sur',
	'04': 'Campeche',
	'05': 'Coahuila de Zaragoza',
	'06': 'Colima',
	'07': 'Chiapas',
	'08': 'Chihuahua',
	'09': 'Distrito Federal',
	'10': 'Durango',
	'11': 'Guanajuato',
	'12': 'Guerrero',
	'13': 'Hidalgo',
	'14': 'Jalisco',
	'15': 'México',
	'16': 'Michoacán de Ocampo',
	'17': 'Morelos',
	'18': 'Nayarit',
	'19': 'Nuevo León',
	'20': 'Oaxaca',
	'21': 'Puebla',
	'22': 'Querétaro',
	'23': 'Quintana Roo',
	'24': 'San Luis Potosí',
	'25': 'Sinaloa',
	'26': 'Sonora',
	'27': 'Tabasco',
	'28': 'Tamaulipas',
	'29': 'Tlaxcala',
	'30': 'Veracruz de Ignacio de la Llave',
	'31': 'Yucatán',
	'32': 'Zacatecas',
	'90': 'Estado sin clasificar',
	'91': 'Migración',
	'92': 'Extranjero'
}


opc_estado = [
	['01',  'Aguascalientes'],
	['02',  'Baja California'],
	['03',  'Baja California Sur'],
	['04',  'Campeche'],
	['05',  'Coahuila de Zaragoza'],
	['06',  'Colima'],
	['07',  'Chiapas'],
	['08',  'Chihuahua'],
	['09',  'Distrito Federal'],
	['10',  'Durango'],
	['11',  'Guanajuato'],
	['12',  'Guerrero'],
	['13',  'Hidalgo'],
	['14',  'Jalisco'],
	['15',  'México'],
	['16',  'Michoacán de Ocampo'],
	['17',  'Morelos'],
	['18',  'Nayarit'],
	['19',  'Nuevo León'],
	['20',  'Oaxaca'],
	['21',  'Puebla'],
	['22',  'Querétaro'],
	['23',  'Quintana Roo'],
	['24',  'San Luis Potosí'],
	['25',  'Sinaloa'],
	['26',  'Sonora'],
	['27',  'Tabasco'],
	['28',  'Tamaulipas'],
	['29',  'Tlaxcala'],
	['30',  'Veracruz de Ignacio de la Llave'],
	['31',  'Yucatán'],
	['32',  'Zacatecas'],
	['90',  'Estado sin clasificar'],
	['91',  'Migración'],
	['92',  'Extranjero']
]


def_periodo = {

	201201: '201201',
	201202: '201202',
	201203: '201203',
	201204: '201204',
	201205: '201205',
	201206: '201206',
	201207: '201207',
	201208: '201208',
	201209: '201209',
	201210: '201210',
	201211: '201211',
	201212: '201212',

	201301: '201301',
	201302: '201302',
	201303: '201303',
	201304: '201304',
	201305: '201305',
	201306: '201306',
	201307: '201307',
	201308: '201308',
	201309: '201309',
	201310: '201310',
	201311: '201311',
	201312: '201312',

	201401: '201401',
	201402: '201402',
	201403: '201403',
	201404: '201404',
	201405: '201405',
	201406: '201406',
	201407: '201407',
	201408: '201408',
	201409: '201409',
	201410: '201410',
	201411: '201411',
	201412: '201412',

	201501: '201501',
	201502: '201502',
	201503: '201503',
	201504: '201504',
	201505: '201505',
	201506: '201506',
	201507: '201507',
	201508: '201508',
	201509: '201509',
	201510: '201510',
	201511: '201511',
	201512: '201512',

	201601: '201601',
	201602: '201602',
	201603: '201603',
	201604: '201604',
	201605: '201605',
	201606: '201606',
	201607: '201607',
	201608: '201608',
	201609: '201609',
	201610: '201610',
	201611: '201611',
	201612: '201612'
}


def_periodo_lead = {

	201201: 'Enero 2012',
	201202: 'Febrero 2012',
	201203: 'Marzo 2012',
	201204: 'Abril 2012',
	201205: 'Mayo 2012',
	201206: 'Junio 2012',
	201207: 'Julio 2012',
	201208: 'Agosto 2012',
	201209: 'Septiembre 2012',
	201210: 'Octubre 2012',
	201211: 'Noviembre 2012',
	201212: 'Diciembre 2012',

	201301: 'Enero 2013',
	201302: 'Febrero 2013',
	201303: 'Marzo 2013',
	201304: 'Abril 2013',
	201305: 'Mayo 2013',
	201306: 'Junio 2013',
	201307: 'Julio 2013',
	201308: 'Agosto 2013',
	201309: 'Septiembre 2013',
	201310: 'Octubre 2013',
	201311: 'Noviembre 2013',
	201312: 'Diciembre 2013',

	201401: 'Enero 2014',
	201402: 'Febrero 2014',
	201403: 'Marzo 2014',
	201404: 'Abril 2014',
	201405: 'Mayo 2014',
	201406: 'Junio 2014',
	201407: 'Julio 2014',
	201408: 'Agosto 2014',
	201409: 'Septiembre 2014',
	201410: 'Octubre 2014',
	201411: 'Noviembre 2014',
	201412: 'Diciembre 2014',

	201501: 'Enero 2015',
	201502: 'Febrero 2015',
	201503: 'Marzo 2015',
	201504: 'Abril 2015',
	201505: 'Mayo 2015',
	201506: 'Junio 2015',
	201507: 'Julio 2015',
	201508: 'Agosto 2015',
	201509: 'Septiembre 2015',
	201510: 'Octubre 2015',
	201511: 'Noviembre 2015',
	201512: 'Diciembre 2015',

	201601: 'Enero 2016',
	201602: 'Febrero 2016',
	201603: 'Marzo 2016',
	201604: 'Abril 2016',
	201605: 'Mayo 2016',
	201606: 'Junio 2016',
	201607: 'Julio 2016',
	201608: 'Agosto 2016',
	201609: 'Septiembre 2016',
	201610: 'Octubre 2016',
	201611: 'Noviembre 2016',
	201612: 'Diciembre 2016',
}

opc_periodo = [

	['201612', '201612'],
	['201611', '201611'],	
	['201610', '201610'],
	['201609', '201609'],
	['201608', '201608'],
	['201607', '201607'],
	['201606', '201606'],
	['201605', '201605'],
	['201604', '201604'],
	['201603', '201603'],
	['201602', '201602'],
	['201601', '201601'],

	['201512', '201512'],
	['201511', '201511'],	
	['201510', '201510'],
	['201509', '201509'],
	['201508', '201508'],
	['201507', '201507'],
	['201506', '201506'],
	['201505', '201505'],
	['201504', '201504'],
	['201503', '201503'],
	['201502', '201502'],
	['201501', '201501'],

	['201412', '201412'],
	['201411', '201411'],	
	['201410', '201410'],
	['201409', '201409'],
	['201408', '201408'],
	['201407', '201407'],
	['201406', '201406'],
	['201405', '201405'],
	['201404', '201404'],
	['201403', '201403'],
	['201402', '201402'],
	['201401', '201401'],

	['201312', '201312'],
	['201311', '201311'],	
	['201310', '201310'],
	['201309', '201309'],
	['201308', '201308'],
	['201307', '201307'],
	['201306', '201306'],
	['201305', '201305'],
	['201304', '201304'],
	['201303', '201303'],
	['201302', '201302'],
	['201301', '201301'],

	['201212', '201212'],
	['201211', '201211'],	
	['201210', '201210'],
	['201209', '201209'],
	['201208', '201208'],
	['201207', '201207'],
	['201206', '201206'],
	['201205', '201205'],
	['201204', '201204'],
	['201203', '201203'],
	['201202', '201202'],
	['201201', '201201']	
]

opc_periodo_y = [
	['201612', '201612'],
	['201512', '201512'],
	['201412', '201412'],
	['201312', '201312'],
	['201212', '201212']
]


def_cliente = {
	'001': 'Cliente 1',
	'002': 'Cliente 2',
	'003': 'Cliente 3',
	'004': 'Cliente 4',
	'005': 'Cliente 5',
	'006': 'Cliente 6',
	'007': 'Cliente 7',
	'008': 'Cliente 8',
	'009': 'Cliente 9',
	'010': 'Cliente 10',
	'011': 'Cliente 11',
	'012': 'Cliente 12',
	'013': 'Cliente 13',
	'014': 'Cliente 14',
	'015': 'Cliente 15',
	'016': 'Cliente 16',
	'017': 'Cliente 17',
	'018': 'Cliente 18',
	'019': 'Cliente 19',
	'020': 'Cliente 20',
	'021': 'Cliente 21',
	'022': 'Cliente 22',
	'023': 'Cliente 23',
	'024': 'Cliente 24',
	'025': 'Cliente 25',
	'026': 'Cliente 26',
	'027': 'Cliente 27',
	'028': 'Cliente 28',
	'029': 'Cliente 29',
	'030': 'Cliente 30',
	'031': 'Cliente 31',
	'032': 'Cliente 32',
	'033': 'Cliente 33',
	'034': 'Cliente 34',
	'035': 'Cliente 35',
	'036': 'Cliente 36',
	'037': 'Cliente 37',
	'038': 'Cliente 38',
	'039': 'Cliente 39',
	'040': 'Cliente 40',
	'041': 'Cliente 41',
	'042': 'Cliente 42',
	'043': 'Cliente 43',
	'044': 'Cliente 44',
	'045': 'Cliente 45',
	'046': 'Cliente 46',
	'047': 'Cliente 47',
	'048': 'Cliente 48',
	'049': 'Cliente 49',
	'050': 'Cliente 50',
	'051': 'Cliente 51',
	'052': 'Cliente 52',
	'053': 'Cliente 53',
	'054': 'Cliente 54',
	'055': 'Cliente 55',
	'056': 'Cliente 56',
	'057': 'Cliente 57',
	'058': 'Cliente 58',
	'059': 'Cliente 59',
	'060': 'Cliente 60',
	'061': 'Cliente 61',
	'062': 'Cliente 62',
	'063': 'Cliente 63',
	'064': 'Cliente 64',
	'065': 'Cliente 65',
	'066': 'Cliente 66',
	'067': 'Cliente 67',
	'068': 'Cliente 68',
	'069': 'Cliente 69',
	'070': 'Cliente 70',
	'071': 'Cliente 71',
	'072': 'Cliente 72',
	'073': 'Cliente 73',
	'074': 'Cliente 74',
	'075': 'Cliente 75',
	'076': 'Cliente 76',
	'077': 'Cliente 77',
	'078': 'Cliente 78',
	'079': 'Cliente 79',
	'080': 'Cliente 80',
	'081': 'Cliente 81',
	'082': 'Cliente 82',
	'083': 'Cliente 83',
	'084': 'Cliente 84',
	'085': 'Cliente 85',
	'086': 'Cliente 86',
	'087': 'Cliente 87',
	'088': 'Cliente 88',
	'089': 'Cliente 89',
	'090': 'Cliente 90',
	'091': 'Cliente 91',
	'092': 'Cliente 92',
	'093': 'Cliente 93',
	'094': 'Cliente 94',
	'095': 'Cliente 95',
	'096': 'Cliente 96',
	'097': 'Cliente 97',
	'098': 'Cliente 98',
	'099': 'Cliente 99',
	'100': 'Cliente 100',
	'101': 'Cliente 101',
	'102': 'Cliente 102',
	'103': 'Cliente 103',
	'104': 'Cliente 104',
	'105': 'Cliente 105',
	'106': 'Cliente 106',
	'107': 'Cliente 107',
	'108': 'Cliente 108',
	'109': 'Cliente 109',
	'110': 'Cliente 110',
	'111': 'Cliente 111',
	'112': 'Cliente 112',
	'113': 'Cliente 113',
	'114': 'Cliente 114',
	'115': 'Cliente 115',
	'116': 'Cliente 116',
	'117': 'Cliente 117',
	'118': 'Cliente 118',
	'119': 'Cliente 119',
	'120': 'Cliente 120',
	'121': 'Cliente 121',
	'122': 'Cliente 122',
	'123': 'Cliente 123',
	'124': 'Cliente 124',
	'125': 'Cliente 125',
	'126': 'Cliente 126',
	'127': 'Cliente 127',
	'128': 'Cliente 128',
	'129': 'Cliente 129',
	'130': 'Cliente 130',
	'131': 'Cliente 131',
	'132': 'Cliente 132',
	'133': 'Cliente 133',
	'134': 'Cliente 134',
	'135': 'Cliente 135',
	'136': 'Cliente 136',
	'137': 'Cliente 137',
	'138': 'Cliente 138',
	'139': 'Cliente 139',
	'140': 'Cliente 140',
	'141': 'Cliente 141',
	'142': 'Cliente 142',
	'143': 'Cliente 143',
	'144': 'Cliente 144',
	'145': 'Cliente 145',
	'146': 'Cliente 146',
	'147': 'Cliente 147',
	'148': 'Cliente 148',
	'149': 'Cliente 149',
	'150': 'Cliente 150',
	'151': 'Cliente 151',
	'152': 'Cliente 152',
	'153': 'Cliente 153',
	'154': 'Cliente 154',
	'155': 'Cliente 155',
	'156': 'Cliente 156',
	'157': 'Cliente 157',
	'158': 'Cliente 158',
	'159': 'Cliente 159',
	'160': 'Cliente 160',
	'161': 'Cliente 161',
	'162': 'Cliente 162',
	'163': 'Cliente 163',
	'164': 'Cliente 164',
	'165': 'Cliente 165',
	'166': 'Cliente 166',
	'167': 'Cliente 167',
	'168': 'Cliente 168',
	'169': 'Cliente 169',
	'170': 'Cliente 170',
	'171': 'Cliente 171',
	'172': 'Cliente 172',
	'173': 'Cliente 173',
	'174': 'Cliente 174',
	'175': 'Cliente 175',
	'176': 'Cliente 176',
	'177': 'Cliente 177',
	'178': 'Cliente 178',
	'179': 'Cliente 179',
	'180': 'Cliente 180',
	'181': 'Cliente 181',
	'182': 'Cliente 182',
	'183': 'Cliente 183',
	'184': 'Cliente 184',
	'185': 'Cliente 185',
	'186': 'Cliente 186',
	'187': 'Cliente 187',
	'188': 'Cliente 188',
	'189': 'Cliente 189',
	'190': 'Cliente 190',
	'191': 'Cliente 191',
	'192': 'Cliente 192',
	'193': 'Cliente 193',
	'194': 'Cliente 194',
	'195': 'Cliente 195',
	'196': 'Cliente 196',
	'197': 'Cliente 197',
	'198': 'Cliente 198',
	'199': 'Cliente 199',
	'200': 'Cliente 200',
	'201': 'Cliente 201',
	'202': 'Cliente 202',
	'203': 'Cliente 203',
	'204': 'Cliente 204',
	'205': 'Cliente 205',
	'206': 'Cliente 206',
	'207': 'Cliente 207',
	'208': 'Cliente 208',
	'209': 'Cliente 209',
	'210': 'Cliente 210',
	'211': 'Cliente 211',
	'212': 'Cliente 212',
	'213': 'Cliente 213',
	'214': 'Cliente 214',
	'215': 'Cliente 215',
	'216': 'Cliente 216',
	'217': 'Cliente 217',
	'218': 'Cliente 218',
	'219': 'Cliente 219',
	'220': 'Cliente 220',
	'221': 'Cliente 221',
	'222': 'Cliente 222',
	'223': 'Cliente 223',
	'224': 'Cliente 224',
	'225': 'Cliente 225',
	'226': 'Cliente 226',
	'227': 'Cliente 227',
	'228': 'Cliente 228',
	'229': 'Cliente 229',
	'230': 'Cliente 230',
	'231': 'Cliente 231',
	'232': 'Cliente 232',
	'233': 'Cliente 233',
	'234': 'Cliente 234',
	'235': 'Cliente 235',
	'236': 'Cliente 236',
	'237': 'Cliente 237',
	'238': 'Cliente 238',
	'239': 'Cliente 239',
	'240': 'Cliente 240',
	'241': 'Cliente 241',
	'242': 'Cliente 242',
	'243': 'Cliente 243',
	'244': 'Cliente 244',
	'245': 'Cliente 245',
	'246': 'Cliente 246',
	'247': 'Cliente 247',
	'248': 'Cliente 248',
	'249': 'Cliente 249',
	'250': 'Cliente 250',
	'251': 'Cliente 251',
	'252': 'Cliente 252',
	'253': 'Cliente 253',
	'254': 'Cliente 254',
	'255': 'Cliente 255',
	'256': 'Cliente 256',
	'257': 'Cliente 257',
	'258': 'Cliente 258',
	'259': 'Cliente 259',
	'260': 'Cliente 260',
	'261': 'Cliente 261',
	'262': 'Cliente 262',
	'263': 'Cliente 263',
	'264': 'Cliente 264',
	'265': 'Cliente 265',
	'266': 'Cliente 266',
	'267': 'Cliente 267',
	'268': 'Cliente 268',
	'269': 'Cliente 269',
	'270': 'Cliente 270',
	'271': 'Cliente 271',
	'272': 'Cliente 272',
	'273': 'Cliente 273',
	'274': 'Cliente 274',
	'275': 'Cliente 275',
	'276': 'Cliente 276',
	'277': 'Cliente 277',
	'278': 'Cliente 278',
	'279': 'Cliente 279',
	'280': 'Cliente 280',
	'281': 'Cliente 281',
	'282': 'Cliente 282',
	'283': 'Cliente 283',
	'284': 'Cliente 284',
	'285': 'Cliente 285',
	'286': 'Cliente 286',
	'287': 'Cliente 287',
	'288': 'Cliente 288',
	'289': 'Cliente 289',
	'290': 'Cliente 290',
	'291': 'Cliente 291',
	'292': 'Cliente 292',
	'293': 'Cliente 293',
	'294': 'Cliente 294',
	'295': 'Cliente 295',
	'296': 'Cliente 296',
	'297': 'Cliente 297',
	'298': 'Cliente 298',
	'299': 'Cliente 299',
	'300': 'Cliente 300',
	'400': 'Cliente 400',
	'500': 'Cliente 500',
	'999': 'Cliente 1000',
	'000': 'Cliente Ultimo'
}


opc_cliente = [
	['001', 'Cliente 1'],
	['002', 'Cliente 2'],
	['003', 'Cliente 3'],
	['004', 'Cliente 4'],
	['005', 'Cliente 5'],
	['006', 'Cliente 6'],
	['007', 'Cliente 7'],
	['008', 'Cliente 8'],
	['009', 'Cliente 9'],
	['010', 'Cliente 10'],
	['011', 'Cliente 11'],
	['012', 'Cliente 12'],
	['013', 'Cliente 13'],
	['014', 'Cliente 14'],
	['015', 'Cliente 15'],
	['016', 'Cliente 16'],
	['017', 'Cliente 17'],
	['018', 'Cliente 18'],
	['019', 'Cliente 19'],
	['020', 'Cliente 20'],
	['030', 'Cliente 30'],
	['040', 'Cliente 40'],
	['050', 'Cliente 50'],
	['060', 'Cliente 60'],
	['070', 'Cliente 70'],
	['080', 'Cliente 80'],
	['090', 'Cliente 90'],
	['100', 'Cliente 100'],
	['110', 'Cliente 110'],
	['120', 'Cliente 120'],
	['130', 'Cliente 130'],
	['140', 'Cliente 140'],
	['150', 'Cliente 150'],
	['160', 'Cliente 160'],
	['170', 'Cliente 170'],
	['180', 'Cliente 180'],
	['190', 'Cliente 190'],
	['200', 'Cliente 200'],
	['300', 'Cliente 300'],
	['400', 'Cliente 400'],
	['500', 'Cliente 500'],
	['999', 'Cliente 1000']
]

def_intervalo = {
	'00': 'Menos de 1 mes',
	'01': '1 mes',
	'02': '2 meses',
	'03': '3 meses',
	'04': '4 meses',
	'05': '5 meses',
	'06': '6 meses',
	'07': '7 a 12 meses',
	'08': '13 a 18 meses',
	'09': '19 a 24 meses',
	'10': '25 a 36 meses',
	'11': '37 a 48 meses',
	'12': '49 a 60 meses',
	'13': '61 a 120 meses',
	'14': 'más de 120',
}

opc_intervalo = [
	# ['00', 'Menos de 1 mes'],
	['01', '1 mes'],
	['02', '2 meses'],
	['03', '3 meses'],
	['04', '4 meses'],
	['05', '5 meses'],
	['06', '6 meses'],
	['07', '7 a 12 meses'],
	['08', '13 a 18 meses'],
	['09', '19 a 24 meses'],
	['10', '25 a 36 meses'],
	['11', '37 a 48 meses'],
	['12', '49 a 60 meses'],
	['13', '61 a 120 meses'],
	['14', 'más de 120']
]


def_monto = {
	'00': 'Sin clasificación',
	'01': '0-10 ',
	'02': '10-25',
	'03': '25-50 ',
	'04': '50-100 ',
	'05': '100-250',
	'06': '250-500',
	'07': '500-1,000',
	'08': '1,000-2,500',
	'09': '2,500-5,000',
	'10': '5,000-10,000',
	'11': '10,000-25,000',
	'12': '25,000-50,000',
	'13': '50,000-100,000',
	'14': '100,000-250,000',
	'15': '250,000-500,000',
	'16': '500,000-1,000,000',
	'17': '1,000,000-2,500,000',
	'18': '2,500,000-5,000,000',
	'19': '+ 5,000,000'
}

opc_monto = [
	['01', '0-10 '],
	['02', '10-25'],
	['03', '25-50 '],
	['04', '50-100 '],
	['05', '100-250'],
	['06', '250-500'],
	['07', '500-1,000'],
	['08', '1,000-2,500'],
	['09', '2,500-5,000'],
	['10', '5,000-10,000'],
	['11', '10,000-25,000'],
	['12', '25,000-50,000'],
	['13', '50,000-100,000'],
	['14', '100,000-250,000'],
	['15', '250,000-500,000'],
	['16', '500,000-1,000,000'],
	['17', '1,000,000-2,500,000'],
	['18', '2,500,000-5,000,000'],
	['19', '+ 5,000,000'],
	['00', 'Sin clasificación']
]


def_moneda = {
	'00':'Nacional',
	'01':'Extranjera',
	'02':'UDIS'
}


opc_moneda = [
	['00', 'Nacional'],
	['01', 'Extranjera'],
	['02', 'UDIS']
]


def_destino_credito = {
	'00': 'No Clasificado',
	'21': 'Consolidacion (pago) de pasivos',
	'22': 'Activo fijo',
	'23': 'Obras publicas',
	'24': 'Proyectos de infraestructura',
	'25': 'Desarrollo Inmobiliario de Vivienda',
	'26': 'Desarrollo Inmobiliario Comercial',
	'27': 'Capital de Trabajo',
	'28': 'Operaciones de Factoraje Financiero',
	'29': 'Operaciones de Arrendamiento Puro',
	'30': 'Operaciones de Arrendamiento Financiero',
	'31': 'Credito a Estados y Municipios',
	'32': 'Credito a Instituciones Financieras',
	'33': 'Procampo'
}

opc_destino_credito = [
	['00', 'No Clasificado'],
	['21', 'Consolidacion (pago) de pasivos'],
	['22', 'Activo fijo'],
	['23', 'Obras publicas'],
	['24', 'Proyectos de infraestructura'],
	['25', 'Desarrollo Inmobiliario de Vivienda'],
	['26', 'Desarrollo Inmobiliario Comercial'],
	['27', 'Capital de Trabajo'],
	['28', 'Operaciones de Factoraje Financiero'],
	['29', 'Operaciones de Arrendamiento Puro'],
	['30', 'Operaciones de Arrendamiento Financiero'],
	['31', 'Credito a Estados y Municipios'],
	['32', 'Credito a Instituciones Financieras'],
	['33', 'Procampo']
]


def_garantia = {
	'00': 'Sin Garantía',
	'01': 'Dinero en Efectivo',
	'02': 'Acciones Representativas de Capital',
	'03': 'Bienes Muebles',
	'04': 'Bienes Inmuebles',
	'05': 'Documentos por Cobrar',
	'06': 'Inventarios o Productos Terminado',
	'07': 'Títulos de Deuda Emitidos por el Gobierno Federal',
	'08': 'Títulos de Deuda Emitidos por Entidades Distintas al Gobierno Federal',
	'09': 'Con Garantía Fiduciaria',
	'10': 'Masa de Garantías'	
}

opc_garantia = [
	['00', 'Sin Garantía'],
	['01', 'Dinero en Efectivo'],
	['02', 'Acciones Representativas de Capital'],
	['03', 'Bienes Muebles'],
	['04', 'Bienes Inmuebles'],
	['05', 'Documentos por Cobrar'],
	['06', 'Inventarios o Productos Terminado'],
	['07', 'Títulos de Deuda Emitidos por el Gobierno Federal'],
	['08', 'Títulos de Deuda Emitidos por Entidades Distintas al Gobierno Federal'],
	['09', 'Con Garantía Fiduciaria'],
	['10', 'Masa de Garantías']
]


def_calificacion = {
	'A1': 'A1',
	'A2': 'A2',
	'B1': 'B1',
	'B2': 'B2',
	'B3': 'B3',
	'CDE': 'C,D,E',
	'PM': 'PM',
	'EX': 'EX'	
}

opc_calificacion = [
	['A1', 'A1'],
	['A2', 'A2'],
	['B1', 'B1'],
	['B2', 'B2'],
	['B3', 'B3'],
	['CDE', 'C,D,E'],
	['PM', 'PM'],
	['EX', 'EX']
]

def_sector = {
	'010': 'Agricultura, Silvicultura, Ganadería y Pesca',
	'020': 'Bancario',
	'030': 'Comercio',
	'040': 'Comunicaciones y Telecomunicaciones',
	'050': 'Construcción',
	'051': 'Edificación residencial',
	'052': 'Otros construcción',
	'060': 'Educativo',
	'070': 'Hoteles y Restaurantes',
	'080': 'Alimentos, Bebidas y Tabaco',
	'090': 'Industria Automotriz',
	'100': 'Petróleo, Minería, Gas y Energía',
	'110': 'Resto Industria',
	'120': 'Salud',
	'130': 'Servicios Comunales y Sociales',
	'140': 'Servicios Financieros (No Bancarios)',
	'150': 'Servicios Profesionales y Técnicos',
	'160': 'Transporte',
	'170': 'Gobierno, Estados y Municipio',
	'180': 'Gobierno Federal',
	'190': 'Organismos Internacionales',
	'200': 'Industria Textil y de Calzado',
	'210': 'Industria Química y Farmacéutica',
	'220': 'Industria Materiales de Construcción',
	'230': 'Servicios de Esparcimiento y otros Servicios Recreativo',
	'999': 'Total'
}

opc_sector = [
	['010', 'Agricultura, Silvicultura, Ganadería y Pesca'],
	['020', 'Bancario'],
	['030', 'Comercio'],
	['040', 'Comunicaciones y Telecomunicaciones'],
	['051', 'Edificación residencial'],
	['052', 'Otros construcción'],
	['060', 'Educativo'],
	['070', 'Hoteles y Restaurantes'],
	['080', 'Alimentos, Bebidas y Tabaco'],
	['090', 'Industria Automotriz'],
	['100', 'Petróleo, Minería, Gas y Energía'],
	['110', 'Resto Industria'],
	['120', 'Salud'],
	['130', 'Servicios Comunales y Sociales'],
	['140', 'Servicios Financieros (No Bancarios)'],
	['150', 'Servicios Profesionales y Técnicos'],
	['160', 'Transporte'],
	['170', 'Gobierno, Estados y Municipio'],
	['180', 'Gobierno Federal'],
	['190', 'Organismos Internacionales'],
	['200', 'Industria Textil y de Calzado'],
	['210', 'Industria Química y Farmacéutica'],
	['220', 'Industria Materiales de Construcción'],
	['230', 'Servicios de Esparcimiento y otros Servicios Recreativo']
]


definiciones = {
	'tipo_valor':def_tipo_valor,
	'institucion':def_institucion, 
	'tec':def_tec,
	'estado': def_estado,
	'periodo': def_periodo,
	'variables': def_variables,
	'cortes': def_cortes, #!
	'cliente': def_cliente,
	'moneda': def_moneda,
	'intervalo': def_intervalo,
	'monto': def_monto,
	'variables_lead': def_variables_lead,
	'periodo_lead': def_periodo_lead,
	'destino':def_destino_credito,
	'garantia': def_garantia,
	'calificacion': def_calificacion,
	'sector': def_sector,
	'secciones': def_secciones,
	'bulk_slide_import': def_bulk_slide_import
}


opciones = {
	'tipo_valor': decode_options(opc_tipo_valor, 'tipo_valor'),
	'institucion': decode_options(opc_institucion, 'institucion'),
	'tec': decode_options(opc_tec, 'tec'),
	'estado': decode_options(opc_estado, 'estado'),
	'periodo': decode_options(opc_periodo, 'periodo'),
	'periodo_y': decode_options(opc_periodo_y, 'periodo_y'),
	'cliente': decode_options(opc_cliente, 'cliente'),
	'intervalo': decode_options(opc_intervalo, 'intervalo'),
	'monto': decode_options(opc_monto, 'monto'),
	'moneda': decode_options(opc_moneda, 'moneda'),
	'destino':decode_options(opc_destino_credito, 'destino'),
	'garantia':decode_options(opc_garantia, 'garantia'),
	'calificacion':decode_options(opc_calificacion, 'calificacion'),
	'sector':decode_options(opc_sector, 'sector'),
	'secciones':decode_options(opc_secciones, 'secciones'),
}


#--- Catalogos CNBV ---
cat_institucion = {
	'5': ['Total Banca Múltiple', '00'],
	'040138': ['ABC Capital', '11'],
	'040133': ['Actinver', '12'],
	'040062': ['Afirme', '13'],
	'040103': ['American Express', '14'],
	'040128': ['Autofin', '15'],
	'040002': ['Banamex', '16'],
	'040042': ['Banca Mifel', '17'],
	'040131': ['Banco Ahorro Famsa', '18'],
	'040127': ['Banco Azteca', '19'],
	'040152': ['Banco Bancrea', '20'],
	'040145': ['Banco Base', '21'],
	'040146': ['Banco Bicentenario', '22'],
	'040126': ['Banco Credit Suisse', '23'],
	'040030': ['Banco del Bajío', '24'],
	'040156': ['Banco Sabadell', '25'],
	'040134': ['Banco Wal-Mart', '26'],
	'040137': ['BanCoppel', '27'],
	'040106': ['Bank of America', '28'],
	'040108': ['Bank of Tokyo-Mitsubishi UFJ', '29'],
	'040147': ['Bankaool', '30'],
	'040072': ['Banorte/Ixe', '31'],
	'040058': ['Banregio', '32'],
	'040060': ['Bansí', '33'],
	'040012': ['BBVA Bancomer', '34'],
	'040143': ['CIBanco', '35'],
	'040140': ['Consubanco', '36'],
	'040124': ['Deutsche Bank', '37'],
	'040151': ['Dondé Banco', '38'],
	'040154': ['Finterra', '39'],
	'040021': ['HSBC', '40'],
	'040155': ['ICBC', '41'],
	'040036': ['Inbursa', '42'],
	'040116': ['ING', '43'],
	'040150': ['Inmobiliario Mexicano', '44'],
	'040037': ['Interacciones', '45'],
	'040136': ['Intercam Banco', '46'],
	'040102': ['Investa Bank', '47'],
	'040059': ['Invex', '48'],
	'040032': ['Ixe', '49'],
	'040110': ['J.P. Morgan', '50'],
	'040112': ['Monex', '51'],
	'040132': ['Multiva', '52'],
	'040014': ['Santander', '53'],
	'040307': ['Santander Vivienda', '54'],
	'040044': ['Scotiabank', '55'],
	'040113': ['Ve por Más', '56'],

	'40138': ['ABC Capital', '11'],
	'40133': ['Actinver', '12'],
	'40062': ['Afirme', '13'],
	'40103': ['American Express', '14'],
	'40128': ['Autofin', '15'],
	'40002': ['Banamex', '16'],
	'40042': ['Banca Mifel', '17'],
	'40131': ['Banco Ahorro Famsa', '18'],
	'40127': ['Banco Azteca', '19'],
	'40152': ['Banco Bancrea', '20'],
	'40145': ['Banco Base', '21'],
	'40146': ['Banco Bicentenario', '22'],
	'40126': ['Banco Credit Suisse', '23'],
	'40030': ['Banco del Bajío', '24'],
	'40156': ['Banco Sabadell', '25'],
	'40134': ['Banco Wal-Mart', '26'],
	'40137': ['BanCoppel', '27'],
	'40106': ['Bank of America', '28'],
	'40108': ['Bank of Tokyo-Mitsubishi UFJ', '29'],
	'40147': ['Bankaool', '30'],
	'40072': ['Banorte/Ixe', '31'],
	'40058': ['Banregio', '32'],
	'40060': ['Bansí', '33'],
	'40012': ['BBVA Bancomer', '34'],
	'40143': ['CIBanco', '35'],
	'40140': ['Consubanco', '36'],
	'40124': ['Deutsche Bank', '37'],
	'40151': ['Dondé Banco', '38'],
	'40154': ['Finterra', '39'],
	'40021': ['HSBC', '40'],
	'40155': ['ICBC', '41'],
	'40036': ['Inbursa', '42'],
	'40116': ['ING', '43'],
	'40150': ['Inmobiliario Mexicano', '44'],
	'40037': ['Interacciones', '45'],
	'40136': ['Intercam Banco', '46'],
	'40102': ['Investa Bank', '47'],
	'40059': ['Invex', '48'],
	'40032': ['Ixe', '49'],
	'40110': ['J.P. Morgan', '50'],
	'40112': ['Monex', '51'],
	'40132': ['Multiva', '52'],
	'40014': ['Santander', '53'],
	'40307': ['Santander Vivienda', '54'],
	'40044': ['Scotiabank', '55'],
	'40113': ['Ve por Más', '56']
}

cat_dato = {
	'3': ['1. Número de Créditos', '04'],
	'4': ['0. Número de Acreditados', '05'],
	'0': ['2. Cartera Total', '01'],
	'1': ['3. Cartera Vigente', '02'],
	'2': ['4. Cartera Vencida', '03'],
}

cat_concepto = {
	'1': ['Número de Créditos', '04'],
	'2': ['Número de Acreditados', '05'],
	'3': ['Tasa de Interés MN', '21'],
	'6': ['Plazo Ponderado en meses (remanente)', '51'],
	'7': ['Responsabilidad Total', '01'],
	'4': ['Tasa de Interés ME', '22'],
	'5': ['Tasa de Interés UDIS', '23']
}


cat_TEC = {
	'1': ['Micro', '01'],
	'2': ['Pequeña', '02'],
	'3': ['Mediana', '03'],
	'4': ['Grande', '04'],
	'5': ['Fideicomiso', '05'],
}


cat_estado = {
	'1': ['Aguascalientes', '01'],
	'2': ['Baja California', '02'],
	'3': ['Baja California Sur', '03'],
	'4': ['Campeche', '04'],
	'5': ['Coahuila de Zaragoza', '05'],
	'6': ['Colima', '06'],
	'7': ['Chiapas', '07'],
	'8': ['Chihuahua', '08'],
	'9': ['Distrito Federal', '09'],
	'10': ['Durango', '10'],
	'11': ['Guanajuato', '11'],
	'12': ['Guerrero', '12'],
	'13': ['Hidalgo', '13'],
	'14': ['Jalisco', '14'],
	'15': ['México', '15'],
	'16': ['Michoacán de Ocampo', '16'],
	'17': ['Morelos', '17'],
	'18': ['Nayarit', '18'],
	'19': ['Nuevo León', '19'],
	'20': ['Oaxaca', '20'],
	'21': ['Puebla', '21'],
	'22': ['Querétaro', '22'],
	'23': ['Quintana Roo', '23'],
	'24': ['San Luis Potosí', '24'],
	'25': ['Sinaloa', '25'],
	'26': ['Sonora', '26'],
	'27': ['Tabasco', '27'],
	'28': ['Tamaulipas', '28'],
	'29': ['Tlaxcala', '29'],
	'30': ['Veracruz de Ignacio de la Llave', '30'],
	'31': ['Yucatán', '31'],
	'32': ['Zacatecas', '32'],
	'88': ['Extranjero', '92'],
	'99': ['Migración', '91'],
	'888': ['Estado sin clasificar', '90'],
	'999': ['Extranjero', '92']
}

cat_concentracion = {
	'Cliente 1': ['Cliente 1', '001'],
	'Cliente 2': ['Cliente 2', '002'],
	'Cliente 3': ['Cliente 3', '003'],
	'Cliente 4': ['Cliente 4', '004'],
	'Cliente 5': ['Cliente 5', '005'],
	'Cliente 6': ['Cliente 6', '006'],
	'Cliente 7': ['Cliente 7', '007'],
	'Cliente 8': ['Cliente 8', '008'],
	'Cliente 9': ['Cliente 9', '009'],
	'Cliente 10': ['Cliente 10', '010'],
	'Cliente 11': ['Cliente 11', '011'],
	'Cliente 12': ['Cliente 12', '012'],
	'Cliente 13': ['Cliente 13', '013'],
	'Cliente 14': ['Cliente 14', '014'],
	'Cliente 15': ['Cliente 15', '015'],
	'Cliente 16': ['Cliente 16', '016'],
	'Cliente 17': ['Cliente 17', '017'],
	'Cliente 18': ['Cliente 18', '018'],
	'Cliente 19': ['Cliente 19', '019'],
	'Cliente 20': ['Cliente 20', '020'],
	'Cliente 21': ['Cliente 21', '021'],
	'Cliente 22': ['Cliente 22', '022'],
	'Cliente 23': ['Cliente 23', '023'],
	'Cliente 24': ['Cliente 24', '024'],
	'Cliente 25': ['Cliente 25', '025'],
	'Cliente 26': ['Cliente 26', '026'],
	'Cliente 27': ['Cliente 27', '027'],
	'Cliente 28': ['Cliente 28', '028'],
	'Cliente 29': ['Cliente 29', '029'],
	'Cliente 30': ['Cliente 30', '030'],
	'Cliente 31': ['Cliente 31', '031'],
	'Cliente 32': ['Cliente 32', '032'],
	'Cliente 33': ['Cliente 33', '033'],
	'Cliente 34': ['Cliente 34', '034'],
	'Cliente 35': ['Cliente 35', '035'],
	'Cliente 36': ['Cliente 36', '036'],
	'Cliente 37': ['Cliente 37', '037'],
	'Cliente 38': ['Cliente 38', '038'],
	'Cliente 39': ['Cliente 39', '039'],
	'Cliente 40': ['Cliente 40', '040'],
	'Cliente 41': ['Cliente 41', '041'],
	'Cliente 42': ['Cliente 42', '042'],
	'Cliente 43': ['Cliente 43', '043'],
	'Cliente 44': ['Cliente 44', '044'],
	'Cliente 45': ['Cliente 45', '045'],
	'Cliente 46': ['Cliente 46', '046'],
	'Cliente 47': ['Cliente 47', '047'],
	'Cliente 48': ['Cliente 48', '048'],
	'Cliente 49': ['Cliente 49', '049'],
	'Cliente 50': ['Cliente 50', '050'],
	'Cliente 51': ['Cliente 51', '051'],
	'Cliente 52': ['Cliente 52', '052'],
	'Cliente 53': ['Cliente 53', '053'],
	'Cliente 54': ['Cliente 54', '054'],
	'Cliente 55': ['Cliente 55', '055'],
	'Cliente 56': ['Cliente 56', '056'],
	'Cliente 57': ['Cliente 57', '057'],
	'Cliente 58': ['Cliente 58', '058'],
	'Cliente 59': ['Cliente 59', '059'],
	'Cliente 60': ['Cliente 60', '060'],
	'Cliente 61': ['Cliente 61', '061'],
	'Cliente 62': ['Cliente 62', '062'],
	'Cliente 63': ['Cliente 63', '063'],
	'Cliente 64': ['Cliente 64', '064'],
	'Cliente 65': ['Cliente 65', '065'],
	'Cliente 66': ['Cliente 66', '066'],
	'Cliente 67': ['Cliente 67', '067'],
	'Cliente 68': ['Cliente 68', '068'],
	'Cliente 69': ['Cliente 69', '069'],
	'Cliente 70': ['Cliente 70', '070'],
	'Cliente 71': ['Cliente 71', '071'],
	'Cliente 72': ['Cliente 72', '072'],
	'Cliente 73': ['Cliente 73', '073'],
	'Cliente 74': ['Cliente 74', '074'],
	'Cliente 75': ['Cliente 75', '075'],
	'Cliente 76': ['Cliente 76', '076'],
	'Cliente 77': ['Cliente 77', '077'],
	'Cliente 78': ['Cliente 78', '078'],
	'Cliente 79': ['Cliente 79', '079'],
	'Cliente 80': ['Cliente 80', '080'],
	'Cliente 81': ['Cliente 81', '081'],
	'Cliente 82': ['Cliente 82', '082'],
	'Cliente 83': ['Cliente 83', '083'],
	'Cliente 84': ['Cliente 84', '084'],
	'Cliente 85': ['Cliente 85', '085'],
	'Cliente 86': ['Cliente 86', '086'],
	'Cliente 87': ['Cliente 87', '087'],
	'Cliente 88': ['Cliente 88', '088'],
	'Cliente 89': ['Cliente 89', '089'],
	'Cliente 90': ['Cliente 90', '090'],
	'Cliente 91': ['Cliente 91', '091'],
	'Cliente 92': ['Cliente 92', '092'],
	'Cliente 93': ['Cliente 93', '093'],
	'Cliente 94': ['Cliente 94', '094'],
	'Cliente 95': ['Cliente 95', '095'],
	'Cliente 96': ['Cliente 96', '096'],
	'Cliente 97': ['Cliente 97', '097'],
	'Cliente 98': ['Cliente 98', '098'],
	'Cliente 99': ['Cliente 99', '099'],
	'Cliente 100': ['Cliente 100', '100'],
	'Cliente 101': ['Cliente 101', '101'],
	'Cliente 102': ['Cliente 102', '102'],
	'Cliente 103': ['Cliente 103', '103'],
	'Cliente 104': ['Cliente 104', '104'],
	'Cliente 105': ['Cliente 105', '105'],
	'Cliente 106': ['Cliente 106', '106'],
	'Cliente 107': ['Cliente 107', '107'],
	'Cliente 108': ['Cliente 108', '108'],
	'Cliente 109': ['Cliente 109', '109'],
	'Cliente 110': ['Cliente 110', '110'],
	'Cliente 111': ['Cliente 111', '111'],
	'Cliente 112': ['Cliente 112', '112'],
	'Cliente 113': ['Cliente 113', '113'],
	'Cliente 114': ['Cliente 114', '114'],
	'Cliente 115': ['Cliente 115', '115'],
	'Cliente 116': ['Cliente 116', '116'],
	'Cliente 117': ['Cliente 117', '117'],
	'Cliente 118': ['Cliente 118', '118'],
	'Cliente 119': ['Cliente 119', '119'],
	'Cliente 120': ['Cliente 120', '120'],
	'Cliente 121': ['Cliente 121', '121'],
	'Cliente 122': ['Cliente 122', '122'],
	'Cliente 123': ['Cliente 123', '123'],
	'Cliente 124': ['Cliente 124', '124'],
	'Cliente 125': ['Cliente 125', '125'],
	'Cliente 126': ['Cliente 126', '126'],
	'Cliente 127': ['Cliente 127', '127'],
	'Cliente 128': ['Cliente 128', '128'],
	'Cliente 129': ['Cliente 129', '129'],
	'Cliente 130': ['Cliente 130', '130'],
	'Cliente 131': ['Cliente 131', '131'],
	'Cliente 132': ['Cliente 132', '132'],
	'Cliente 133': ['Cliente 133', '133'],
	'Cliente 134': ['Cliente 134', '134'],
	'Cliente 135': ['Cliente 135', '135'],
	'Cliente 136': ['Cliente 136', '136'],
	'Cliente 137': ['Cliente 137', '137'],
	'Cliente 138': ['Cliente 138', '138'],
	'Cliente 139': ['Cliente 139', '139'],
	'Cliente 140': ['Cliente 140', '140'],
	'Cliente 141': ['Cliente 141', '141'],
	'Cliente 142': ['Cliente 142', '142'],
	'Cliente 143': ['Cliente 143', '143'],
	'Cliente 144': ['Cliente 144', '144'],
	'Cliente 145': ['Cliente 145', '145'],
	'Cliente 146': ['Cliente 146', '146'],
	'Cliente 147': ['Cliente 147', '147'],
	'Cliente 148': ['Cliente 148', '148'],
	'Cliente 149': ['Cliente 149', '149'],
	'Cliente 150': ['Cliente 150', '150'],
	'Cliente 151': ['Cliente 151', '151'],
	'Cliente 152': ['Cliente 152', '152'],
	'Cliente 153': ['Cliente 153', '153'],
	'Cliente 154': ['Cliente 154', '154'],
	'Cliente 155': ['Cliente 155', '155'],
	'Cliente 156': ['Cliente 156', '156'],
	'Cliente 157': ['Cliente 157', '157'],
	'Cliente 158': ['Cliente 158', '158'],
	'Cliente 159': ['Cliente 159', '159'],
	'Cliente 160': ['Cliente 160', '160'],
	'Cliente 161': ['Cliente 161', '161'],
	'Cliente 162': ['Cliente 162', '162'],
	'Cliente 163': ['Cliente 163', '163'],
	'Cliente 164': ['Cliente 164', '164'],
	'Cliente 165': ['Cliente 165', '165'],
	'Cliente 166': ['Cliente 166', '166'],
	'Cliente 167': ['Cliente 167', '167'],
	'Cliente 168': ['Cliente 168', '168'],
	'Cliente 169': ['Cliente 169', '169'],
	'Cliente 170': ['Cliente 170', '170'],
	'Cliente 171': ['Cliente 171', '171'],
	'Cliente 172': ['Cliente 172', '172'],
	'Cliente 173': ['Cliente 173', '173'],
	'Cliente 174': ['Cliente 174', '174'],
	'Cliente 175': ['Cliente 175', '175'],
	'Cliente 176': ['Cliente 176', '176'],
	'Cliente 177': ['Cliente 177', '177'],
	'Cliente 178': ['Cliente 178', '178'],
	'Cliente 179': ['Cliente 179', '179'],
	'Cliente 180': ['Cliente 180', '180'],
	'Cliente 181': ['Cliente 181', '181'],
	'Cliente 182': ['Cliente 182', '182'],
	'Cliente 183': ['Cliente 183', '183'],
	'Cliente 184': ['Cliente 184', '184'],
	'Cliente 185': ['Cliente 185', '185'],
	'Cliente 186': ['Cliente 186', '186'],
	'Cliente 187': ['Cliente 187', '187'],
	'Cliente 188': ['Cliente 188', '188'],
	'Cliente 189': ['Cliente 189', '189'],
	'Cliente 190': ['Cliente 190', '190'],
	'Cliente 191': ['Cliente 191', '191'],
	'Cliente 192': ['Cliente 192', '192'],
	'Cliente 193': ['Cliente 193', '193'],
	'Cliente 194': ['Cliente 194', '194'],
	'Cliente 195': ['Cliente 195', '195'],
	'Cliente 196': ['Cliente 196', '196'],
	'Cliente 197': ['Cliente 197', '197'],
	'Cliente 198': ['Cliente 198', '198'],
	'Cliente 199': ['Cliente 199', '199'],
	'Cliente 200': ['Cliente 200', '200'],
	'Cliente 201': ['Cliente 201', '201'],
	'Cliente 202': ['Cliente 202', '202'],
	'Cliente 203': ['Cliente 203', '203'],
	'Cliente 204': ['Cliente 204', '204'],
	'Cliente 205': ['Cliente 205', '205'],
	'Cliente 206': ['Cliente 206', '206'],
	'Cliente 207': ['Cliente 207', '207'],
	'Cliente 208': ['Cliente 208', '208'],
	'Cliente 209': ['Cliente 209', '209'],
	'Cliente 210': ['Cliente 210', '210'],
	'Cliente 211': ['Cliente 211', '211'],
	'Cliente 212': ['Cliente 212', '212'],
	'Cliente 213': ['Cliente 213', '213'],
	'Cliente 214': ['Cliente 214', '214'],
	'Cliente 215': ['Cliente 215', '215'],
	'Cliente 216': ['Cliente 216', '216'],
	'Cliente 217': ['Cliente 217', '217'],
	'Cliente 218': ['Cliente 218', '218'],
	'Cliente 219': ['Cliente 219', '219'],
	'Cliente 220': ['Cliente 220', '220'],
	'Cliente 221': ['Cliente 221', '221'],
	'Cliente 222': ['Cliente 222', '222'],
	'Cliente 223': ['Cliente 223', '223'],
	'Cliente 224': ['Cliente 224', '224'],
	'Cliente 225': ['Cliente 225', '225'],
	'Cliente 226': ['Cliente 226', '226'],
	'Cliente 227': ['Cliente 227', '227'],
	'Cliente 228': ['Cliente 228', '228'],
	'Cliente 229': ['Cliente 229', '229'],
	'Cliente 230': ['Cliente 230', '230'],
	'Cliente 231': ['Cliente 231', '231'],
	'Cliente 232': ['Cliente 232', '232'],
	'Cliente 233': ['Cliente 233', '233'],
	'Cliente 234': ['Cliente 234', '234'],
	'Cliente 235': ['Cliente 235', '235'],
	'Cliente 236': ['Cliente 236', '236'],
	'Cliente 237': ['Cliente 237', '237'],
	'Cliente 238': ['Cliente 238', '238'],
	'Cliente 239': ['Cliente 239', '239'],
	'Cliente 240': ['Cliente 240', '240'],
	'Cliente 241': ['Cliente 241', '241'],
	'Cliente 242': ['Cliente 242', '242'],
	'Cliente 243': ['Cliente 243', '243'],
	'Cliente 244': ['Cliente 244', '244'],
	'Cliente 245': ['Cliente 245', '245'],
	'Cliente 246': ['Cliente 246', '246'],
	'Cliente 247': ['Cliente 247', '247'],
	'Cliente 248': ['Cliente 248', '248'],
	'Cliente 249': ['Cliente 249', '249'],
	'Cliente 250': ['Cliente 250', '250'],
	'Cliente 251': ['Cliente 251', '251'],
	'Cliente 252': ['Cliente 252', '252'],
	'Cliente 253': ['Cliente 253', '253'],
	'Cliente 254': ['Cliente 254', '254'],
	'Cliente 255': ['Cliente 255', '255'],
	'Cliente 256': ['Cliente 256', '256'],
	'Cliente 257': ['Cliente 257', '257'],
	'Cliente 258': ['Cliente 258', '258'],
	'Cliente 259': ['Cliente 259', '259'],
	'Cliente 260': ['Cliente 260', '260'],
	'Cliente 261': ['Cliente 261', '261'],
	'Cliente 262': ['Cliente 262', '262'],
	'Cliente 263': ['Cliente 263', '263'],
	'Cliente 264': ['Cliente 264', '264'],
	'Cliente 265': ['Cliente 265', '265'],
	'Cliente 266': ['Cliente 266', '266'],
	'Cliente 267': ['Cliente 267', '267'],
	'Cliente 268': ['Cliente 268', '268'],
	'Cliente 269': ['Cliente 269', '269'],
	'Cliente 270': ['Cliente 270', '270'],
	'Cliente 271': ['Cliente 271', '271'],
	'Cliente 272': ['Cliente 272', '272'],
	'Cliente 273': ['Cliente 273', '273'],
	'Cliente 274': ['Cliente 274', '274'],
	'Cliente 275': ['Cliente 275', '275'],
	'Cliente 276': ['Cliente 276', '276'],
	'Cliente 277': ['Cliente 277', '277'],
	'Cliente 278': ['Cliente 278', '278'],
	'Cliente 279': ['Cliente 279', '279'],
	'Cliente 280': ['Cliente 280', '280'],
	'Cliente 281': ['Cliente 281', '281'],
	'Cliente 282': ['Cliente 282', '282'],
	'Cliente 283': ['Cliente 283', '283'],
	'Cliente 284': ['Cliente 284', '284'],
	'Cliente 285': ['Cliente 285', '285'],
	'Cliente 286': ['Cliente 286', '286'],
	'Cliente 287': ['Cliente 287', '287'],
	'Cliente 288': ['Cliente 288', '288'],
	'Cliente 289': ['Cliente 289', '289'],
	'Cliente 290': ['Cliente 290', '290'],
	'Cliente 291': ['Cliente 291', '291'],
	'Cliente 292': ['Cliente 292', '292'],
	'Cliente 293': ['Cliente 293', '293'],
	'Cliente 294': ['Cliente 294', '294'],
	'Cliente 295': ['Cliente 295', '295'],
	'Cliente 296': ['Cliente 296', '296'],
	'Cliente 297': ['Cliente 297', '297'],
	'Cliente 298': ['Cliente 298', '298'],
	'Cliente 299': ['Cliente 299', '299'],
	'Cliente 300': ['Cliente 300', '300'],
	'Cliente 400': ['Cliente 400', '400'],
	'Cliente 500': ['Cliente 500', '500'],
	'Cliente 1000': ['Cliente 1000', '999'],
	'Cliente Ultimo': ['Cliente Ultimo', '000']
}

cat_intervalo = {
	'0': ['Menos de 1 mes', '00'],
	'1': ['1 mes', '01'],
	'2': ['2 meses', '02'],
	'3': ['3 meses', '03'],
	'4': ['4 meses', '04'],
	'5': ['5 meses', '05'],
	'6': ['6 meses', '06'],
	'7': ['7 a 12 meses', '07'],
	'8': ['13 a 18 meses', '08'],
	'9': ['19 a 24 meses', '09'],
	'10': ['25 a 36 meses', '10'],
	'11': ['37 a 48 meses', '11'],
	'12': ['49 a 60 meses', '12'],
	'13': ['61 a 120 meses', '13'],
	'14': ['más de 120', '14']
}

cat_monto = {
	'0': ['Sin clasificación', '00'],
	'1': ['0-10 ', '01'],
	'2': ['10-25', '02'],
	'3': ['25-50 ', '03'],
	'4': ['50-100 ', '04'],
	'5': ['100-250', '05'],
	'6': ['250-500', '06'],
	'7': ['500-1,000', '07'],
	'8': ['1,000-2,500', '08'],
	'9': ['2,500-5,000', '09'],
	'10': ['5,000-10,000', '10'],
	'11': ['10,000-25,000', '11'],
	'12': ['25,000-50,000', '12'],
	'13': ['50,000-100,000', '13'],
	'14': ['100,000-250,000', '14'],
	'15': ['250,000-500,000', '15'],
	'16': ['500,000-1,000,000', '16'],
	'17': ['1,000,000-2,500,000', '17'],
	'18': ['2,500,000-5,000,000', '18'],
	'19': ['+ 5,000,000', '19']
}

cat_moneda = {
	'0':['Nacional', '00'],
	'1':['Extranjera', '01'],
	'2':['UDIS', '02']
}

cat_destino_credito = {
	'0': ['No Clasificado', '00'],
	'21': ['Consolidacion (pago) de pasivos', '21'],
	'22': ['Activo fijo', '22'],
	'23': ['Obras publicas', '23'],
	'24': ['Proyectos de infraestructura', '24'],
	'25': ['Desarrollo Inmobiliario de Vivienda', '25'],
	'26': ['Desarrollo Inmobiliario Comercial', '26'],
	'27': ['Capital de Trabajo', '27'],
	'28': ['Operaciones de Factoraje Financiero', '28'],
	'29': ['Operaciones de Arrendamiento Puro', '29'],
	'30': ['Operaciones de Arrendamiento Financiero', '30'],
	'31': ['Credito a Estados y Municipios', '31'],
	'32': ['Credito a Instituciones Financieras', '32'],
	'33': ['Procampo', '33']
}

cat_garantia = {
	'0': ['Sin Garantía', '00'],
	'1': ['Dinero en Efectivo', '01'],
	'2': ['Acciones Representativas de Capital', '02'],
	'3': ['Bienes Muebles', '03'],
	'4': ['Bienes Inmuebles', '04'],
	'5': ['Documentos por Cobrar', '05'],
	'6': ['Inventarios o Productos Terminado', '06'],
	'7': ['Títulos de Deuda Emitidos por el Gobierno Federal', '07'],
	'8': ['Títulos de Deuda Emitidos por Entidades Distintas al Gobierno Federal', '08'],
	'9': ['Con Garantía Fiduciaria', '09'],
	'10': ['Masa de Garantías', '10']	
}

cat_calificacion = {
	'A1': ['A1', 'A1'],
	'A2': ['A2', 'A2'],
	'B1': ['B1', 'B1'],
	'B2': ['B2', 'B2'],
	'B3': ['B3', 'B3'],
	'CDE': ['C,D,E', 'CDE'],
	'PM': ['PM', 'PM'],
	'EX': ['EX', 'EX']
}

cat_sector = {
	'1': ['Agricultura, Silvicultura, Ganadería y Pesca', '010'],
	'2': ['Bancario', '020'],
	'3': ['Comercio', '030'],
	'4': ['Comunicaciones y Telecomunicaciones', '040'],
	'5': ['Construcción', '050'],
	'6': ['Educativo', '060'],
	'7': ['Hoteles y Restaurantes', '070'],
	'8': ['Alimentos, Bebidas y Tabaco', '080'],
	'9': ['Industria Automotriz', '090'],
	'10': ['Petróleo, Minería, Gas y Energía', '100'],
	'11': ['Resto Industria', '110'],
	'12': ['Salud', '120'],
	'13': ['Servicios Comunales y Sociales', '130'],
	'14': ['Servicios Financieros (No Bancarios)', '140'],
	'15': ['Servicios Profesionales y Técnicos', '150'],
	'16': ['Transporte', '160'],
	'17': ['Gobierno, Estados y Municipio', '170'],
	'18': ['Gobierno Federal', '180'],
	'19': ['Organismos Internacionales', '190'],
	'20': ['Industria Textil y de Calzado', '200'],
	'21': ['Industria Química y Farmacéutica', '210'],
	'22': ['Industria Materiales de Construcción', '220'],
	'23': ['Servicios de Esparcimiento y otros Servicios Recreativo', '230'],
	'999': ['Total', '999'],
	'5999': ['Otros construcción', '052'],
	'23611': ['Edificación residencial', '051']
}

#--- trasformation maps ---
tm_040_11A_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'Concentracion':['cliente', cat_concentracion ],
	'Monto_Acumulado':['saldo_acum'],
	'Participacion_Acumulada':['porc_acum'],
	'concentracion_cartera':['concentracion_cartera'], #Dummy field
}



tm_040_11A_R4 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],
	'cve_concepto': ['tipo_valor', cat_concepto],
	'dato': ['valor']
}

tm_040_11A_R8 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],
	'cve_concepto': ['tipo_valor', cat_concepto],
	'dato': ['valor']
}


tm_mod_11C_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],

	'intervalo_responsabilidad':['monto', cat_monto],
	'creditos': ['creditos'],	
	'cart_total': ['saldo_total'],
	'IMOR': ['imor']
}

tm_mod_11C_R2 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_grupo':['monto', cat_monto],
	'cve_tipo_moneda': ['moneda', cat_moneda],

	'plazo_venc':['plazo'],
	'plazo':['vigencia'],
	'tasa': ['tasa']	
}

tm_mod_11D_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'sector': ['sector', cat_sector],

	'm_total': ['saldo_total'],
	'imor': ['imor'],
	'creditos': ['creditos'],
	'acreditados': ['acreditados']
	
}

tm_mod_11D_R2 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'sector': ['sector', cat_sector],
	'cve_tipo_moneda': ['moneda', cat_moneda],

	'plazo_venc':['plazo'],
	'plazo':['vigencia'],
	'tasa': ['tasa']	
}


tm_mod0_11E_R1 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],	
	'calificacion':['calificacion', cat_calificacion],
	'm_total':['saldo_total'],
	'imor': ['imor']
}

tm_mod_11E_R1 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],	
	'imor': ['imor']
}

tm_mod_11E_R3 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],	
	'calificacion':['calificacion', cat_calificacion],
	'n_total': ['creditos']
}

tm_mod_11E_R5 = {
	'cve_institucion': ['institucion', cat_institucion],
	'cve_periodo': ['periodo'],	
	
	'cve_tipo_moneda': ['moneda', cat_moneda],
	'calificacion':['calificacion', cat_calificacion],
	'tasa': ['tasa']
}


tm_040_11F_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],

	'id':['intervalo', cat_intervalo],
	'tasa': ['tasa']	
}


tm_040_11F_R2 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],

	'id':['intervalo', cat_intervalo],
	'creditos': ['creditos'],	
	'monto_dispuesto': ['saldo_total']
}


tm_mod_11G_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_estado': ['estado', cat_estado],
	'cartera_total': ['saldo_total'],

	'imor': ['imor'],
	'creditos': ['creditos'],
	'acreditados': ['acreditados']
	
}


tm_mod_11K_R1 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],

	'cve_tipo_garantia':['garantia', cat_garantia],
	'creditos': ['creditos'],	
	'total': ['saldo_total'],
	'imor': ['imor']
}


tm_mod_11K_R20 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],

	'cve_tipo_garantia':['garantia', cat_garantia],
	'tasa_ponderada':  ['tasa'],
	'cve_tipo_moneda': ['moneda', cat_moneda]	
}


tm_040_11L_R0 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_TEC': ['tec', cat_TEC],
	'cve_dato':['tipo_valor', cat_dato],
	'saldo': ['valor']
}


tm_040_11L_R2 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],
	'cve_TEC': ['tec', cat_TEC],

	'tasa': ['tasa'],
	'responsabilidad':['saldo_total'],
	'plazo':['plazo']
}

tm_040_11L_R3 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_estado': ['estado', cat_estado],
	'cve_TEC': ['tec', cat_TEC],
	'dat_id_credito_met_cnbv': ['creditos'],
	'dat_rfc': ['acreditados'],
	'dat_responsabilidad_total': ['saldo_total']
}


tm_040_11L_R5 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_TEC': ['tec', cat_TEC],
	'cve_destino_credito': ['destino', cat_destino_credito],
	'dat_responsabilidad_total': ['saldo_total']
}


tm_040_11L_R6 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],
	'cve_destino_credito': ['destino', cat_destino_credito],
	'cve_TEC': ['tec', cat_TEC],

	'tasa': ['tasa'],
	'responsabilidad':['saldo_total'],
	'plazo':['plazo']
}

tm_add0_11L_R6 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],

	'tasa': ['tasa'],
	'responsabilidad':['saldo_total'],
	'plazo':['plazo']
}

tm_add_11L_R6 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],
	'cve_destino_credito': ['destino', cat_destino_credito],

	'tasa': ['tasa'],
	'responsabilidad':['saldo_total'],
	'plazo':['plazo']
}


tm_040_11L_R11 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_TEC': ['tec', cat_TEC],
	'creditos': ['creditos'],
	'acreditados': ['acreditados'],
	'monto_dispuesto': ['saldo_total']
}


tm_040_11L_R12 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_tipo_moneda': ['moneda', cat_moneda],
	'cve_TEC': ['tec', cat_TEC],

	'tasa': ['tasa'],
	'MDMC':['saldo_total'],
	'plazo':['plazo']
}

tm_040_11L_R13 = {
	'cve_periodo': ['periodo'],
	'cve_institucion': ['institucion', cat_institucion],
	'cve_estado': ['estado', cat_estado],
	'cve_TEC': ['tec', cat_TEC],
	'dat_id_credito_met_cnbv': ['creditos'],
	'dat_rfc': ['acreditados'],
	'MDMC': ['saldo_total']
}


transformation_maps_CNBV = {
	'040_11A_R1': tm_040_11A_R1,
	'040_11A_R4': tm_040_11A_R4,
	'040_11A_R8': tm_040_11A_R8,

	'mod_11C_R1': tm_mod_11C_R1,
	'mod_11C_R2': tm_mod_11C_R2,

	'mod_11D_R1': tm_mod_11D_R1,
	'mod_11D_R2': tm_mod_11D_R2,

	'mod0_11E_R1': tm_mod0_11E_R1,
	'mod_11E_R1': tm_mod_11E_R1,
	'mod_11E_R3': tm_mod_11E_R3,
	'mod_11E_R5': tm_mod_11E_R5,

	'040_11F_R1': tm_040_11F_R1,
	'040_11F_R2': tm_040_11F_R2,

	'mod_11G_R1': tm_mod_11G_R1,

	'mod_11K_R1': tm_mod_11K_R1,
	'mod_11K_R20': tm_mod_11K_R20,

	'040_11L_R0': tm_040_11L_R0,
	'040_11L_R2': tm_040_11L_R2,
	'040_11L_R3': tm_040_11L_R3,
	'040_11L_R5': tm_040_11L_R5,
	
	'add0_11L_R6': tm_add0_11L_R6,
	'add_11L_R6': tm_add_11L_R6,
	'040_11L_R6': tm_040_11L_R6,

	'040_11L_R11': tm_040_11L_R11,
	'040_11L_R12': tm_040_11L_R12,
	'040_11L_R13': tm_040_11L_R13,
}



detalles_tabla = {
	'040_11A_R1': {'tipo_variables': 'semi_directas', 'perspectiva': 'total'},

	# '040_11A_R4': {'tipo_variables': 'indirectas', 'perspectiva': 'total'},
	
	# '040_11A_R8': {'tipo_variables': 'indirectas', 'perspectiva': 'marginal'}, #Por lo pronto solo queda fuera de forma temporal.

	'mod_11C_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11C_R2': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11D_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11D_R2': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod0_11E_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11E_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11E_R3': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11E_R5': {'tipo_variables': 'directas', 'perspectiva': 'total'},
	
	'040_11F_R1': {'tipo_variables': 'directas', 'perspectiva': 'marginal'},

	'040_11F_R2': {'tipo_variables': 'directas', 'perspectiva': 'marginal'},

	'mod_11G_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11K_R1': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'mod_11K_R20': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'040_11L_R0': {'tipo_variables': 'indirectas', 'perspectiva': 'total'},
	
	'040_11L_R2': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'040_11L_R3': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'040_11L_R5': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'add0_11L_R6': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'add_11L_R6': {'tipo_variables': 'directas', 'perspectiva': 'total'},
	
	'040_11L_R6': {'tipo_variables': 'directas', 'perspectiva': 'total'},

	'040_11L_R11': {'tipo_variables': 'directas', 'perspectiva': 'marginal'},

	'040_11L_R12': {'tipo_variables': 'directas', 'perspectiva': 'marginal'},

	'040_11L_R13': {'tipo_variables': 'directas', 'perspectiva': 'marginal'}
}


tablas_CNBV = [
	'add0_11L_R6',
	'mod_11E_R1',
	'mod0_11E_R1',
	'mod_11E_R3',
	'mod_11E_R5',

	'040_11A_R1',
	# '040_11A_R4',
	# '040_11A_R8',

	'mod_11C_R1',
	'mod_11C_R2',
	
	'mod_11D_R1',
	'mod_11D_R2',

	'040_11F_R1',
	'040_11F_R2',
	
	'mod_11G_R1',

	'mod_11K_R1',
	'mod_11K_R20',

	'040_11L_R0',
	'040_11L_R2',
	'040_11L_R3',
	'040_11L_R5',
	
	'add_11L_R6',
	'040_11L_R6',

	'040_11L_R11',
	'040_11L_R12',
	'040_11L_R13'
]


demo_version_details = {
	'040_11A_R1': {
		'descripcion':'Cartera actividad empresarial: concentracion del portafolio total por numero de acreditados', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	# '040_11A_R4': {
	# 	'descripcion':'Cartera actividad empresarial: tasa de interes promedio ponderada, portafolio total', 
	# 	'url_fuente': 'Un URL',
	# 	'registros': 0
	# },

	'mod_11C_R1': {
		'descripcion':'Cartera actividad empresarial: numero, saldo e IMOR por intervalo de monto de credito. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod_11C_R2': {
		'descripcion':'Cartera actividad empresarial: tasa por monto del credito. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod_11D_R1': {
		'descripcion':'Cartera actividad empresarial: numero de creditos y saldo de cartera por sector economico. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod_11D_R2': {
		'descripcion':'Cartera actividad empresarial: tasa por sector economico. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod0_11E_R1': {
		'descripcion':'Cartera actividad empresarial: saldo de cartera por calificación. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod_11E_R1': {
		'descripcion':'Cartera actividad empresarial: Índice de morosidad', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	'mod_11E_R3': {
		'descripcion':'Cartera actividad empresarial: número de creditos por calificacion. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	'mod_11E_R5': {
		'descripcion':'Cartera actividad empresarial: tasa por calificación. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	# '040_11A_R8': {
	# 	'descripcion':'Cartera actividad empresarial: Caracteristicas promedio de los creditos dispuestos marginalmente', 
	# 	'url_fuente': 'Un URL',
	# 	'registros': 0
	# },

	'040_11F_R1': {
		'descripcion':'Cartera actividad empresarial: tasa de interés por intervalo de plazo. Creditos dispuestos marginalmente', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11F_R2': {
		'descripcion':'Creditos y saldos por intervalo de plazo. Creditos dispuestos marginalmente', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	'mod_11G_R1': {
		'descripcion':'Cartera actividad empresarial: numero de créditos y saldo de cartera por estado. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'mod_11K_R1': {
		'descripcion':'Cartera actividad empresarial: número de créditos y saldos de cartera por tipo de garantía. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	
	'mod_11K_R20': {
		'descripcion':'Cartera actividad empresarial: tasa de interes por tipo de garantia. Portafolio total', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	'040_11L_R0': {
		'descripcion':'Numero de creditos, acreditados y saldo por tamano de empresa', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R2': {
		'descripcion':'Cartera actividad empresarial: tasas de interes, plazos y saldo por tamano de empresa', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	
	'040_11L_R3': {
		'descripcion':'Distribucion geografica del numero de creditos, acreditados y saldo por tamano de empresa', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R5': {
		'descripcion':'Saldo por destino del credito y tamano de empresa', 
		'url_fuente': 'Un URL',
		'registros': 0
	},


	'add0_11L_R6': {
		'descripcion':'Tasa de interés, plazos y saldo', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'add_11L_R6': {
		'descripcion':'Tasa de interés, plazos y saldo por destino del crédito', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R6': {
		'descripcion':'Tasa de interés, plazos y saldo por destino del crédito y tamaño de empresa', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R11': {
		'descripcion':'Numero de creditos, acreditados y monto por tamano de empresa. Creditos dispuestos marginalmente.', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R12': {
		'descripcion':'Cartera actividad empresarial: tasas de interes, plazos y saldo por tamano de empresa [Marginal]', 
		'url_fuente': 'Un URL',
		'registros': 0
	},

	'040_11L_R13': {
		'descripcion':' Distribucion geografica del numero de creditos, acreditados y monto por tamano de empresa. [Marginal]', 
		'url_fuente': 'Un URL',
		'registros': 0
	}
}



def generar_indice_CNBV(lista_tablas):
	
	indice_CNBV = []

	campos_variables = ['saldo_total', 'creditos', 'acreditados', 'concentracion_cartera', 'porc_acum', 'saldo_acum', 'tasa', 'plazo', 'imor'] # tipo_valor
	campos_cortes = ['periodo', 'institucion', 'tec', 'estado', 'cliente', 'intervalo', 'monto', 'moneda', 'destino', 'garantia', 'calificacion', 'sector']

	for tabla in lista_tablas:
		variables = []
		cortes = []
		tm = transformation_maps_CNBV[tabla]		
		for key, value in tm.iteritems():
			attr = value[0]
			if attr in campos_variables:
				variables.append(attr)
			elif attr in campos_cortes:
				cortes.append(attr)
			elif attr == 'tipo_valor':
				for cve, detalle in value[1].iteritems():
					variables.append(cat_variables[detalle[1]])

		indice_CNBV.append([tabla, variables, cortes, detalles_tabla[tabla]['tipo_variables'], detalles_tabla[tabla]['perspectiva']])

	return indice_CNBV




def definir_opciones_iniciales(indice_CNBV):
	variables = []
	cortes = []
	variables_output = []
	cortes_output = []

	for tabla in indice_CNBV:
		variables_tabla = tabla[1]
		cortes_tabla = tabla[2]
		for variable in variables_tabla:
			if variable not in variables:
				variables.append(variable)
				
		for corte in cortes_tabla:
			if corte not in cortes:
				cortes.append(corte)				

	for variable in opc_variables:
		if variable in variables:
			variables_output.append((variable, def_variables[variable]))

	for corte in opc_cortes:
		if corte in cortes:
			cortes_output.append((corte, def_cortes[corte]))

	opciones_validas = {
		'variables': variables_output,
		'cortes': cortes_output
	}

	return opciones_validas


indice_inicial = generar_indice_CNBV(tablas_CNBV)

opciones_iniciales = definir_opciones_iniciales(indice_inicial)

def invert_dictionary(dictionary):
	result = {}
	for key, value in dictionary.iteritems():
		result[value] = key
	return result

cat_invertida_variables = invert_dictionary(cat_variables)


