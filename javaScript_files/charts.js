var seconds = 0, minutes = 0, hours = 0, limite_periodos = 1, limite_instituciones = 7, denominador_actual = 1,   
    start_time,
    t,
    chart_url,
    chart_units,
    csvContent,
    unmodified_chart_array,
    chart_array,
    chart_type;



function add() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }
    
    console.log((hours ? (hours > 9 ? hours : "0" + hours) : "00") + ":" + (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds));
    timer();
}

function timer() {
    t = setTimeout(add, 1000);
}



$('.ExpandColapseSection').on('click', function(){
  var target_section = $(this).attr("targetsection")
  $(target_section).toggleClass('hidden');

  var GlaphiconDiv = $(this).find('#PlusMinusGlyphicon');
  GlaphiconDiv.toggleClass('glyphicon-minus');
  GlaphiconDiv.toggleClass('glyphicon-plus'); 
});

// xx
$('.SeleccionarCorte').on('click', function(){

  var CorteSeleccionado = $(this)
  console.log(' ')
  console.log('Apretado: ' + CorteSeleccionado.attr('value'))

  var CortesActivos = parseInt($('#NumeroCortesSeleccionados').val());
  var CorteRenglones = $('#CorteRenglones');
  var CorteColumnas = $('#CorteColumnas');

  validar_compatibilidad(CorteSeleccionado, CorteColumnas);

  if (CorteSeleccionado.attr("corte_activo") == "Si") {
    $('#NumeroCortesSeleccionados').val(CortesActivos - 1);
    
    if(CorteSeleccionado.attr('value') == CorteRenglones){
      CorteRenglones.val(CorteColumnas.val())
    }

    CorteColumnas.val('')

  } else {

    if ( CortesActivos == 0){
      CorteRenglones.val(CorteSeleccionado.val());
      $('#NumeroCortesSeleccionados').val(1);

    } else if (CortesActivos == 1) {    
      CorteColumnas.val(CorteSeleccionado.val());
      $('#NumeroCortesSeleccionados').val(2);   

    } else if (CortesActivos == 2){
      flipear_boton_corte(CorteRenglones.val())
      CorteRenglones.val(CorteColumnas.val())
      CorteColumnas.val(CorteSeleccionado.val())         
    }

  }

  console.log('Cortes activos: ' + $('#NumeroCortesSeleccionados').val())
  console.log('Corte columnas: ' + CorteColumnas.val())
  console.log('Corte renglones: ' + CorteRenglones.val())


  flipear_boton_corte(CorteSeleccionado.val());
});



function flipear_boton_corte(nombre_corte) {
  var boton_corte = $('#boton_' + nombre_corte);

  boton_corte.find('#OkGlyphicon').toggleClass('hidden'); 
  boton_corte.toggleClass('btn-primary');
  boton_corte.toggleClass('btn-default');

  if (boton_corte.attr("corte_activo") == "Si") {
    boton_corte.attr("corte_activo", "No"); 
  } else {
    boton_corte.attr("corte_activo", "Si");
  }

  var boton_PlusMinus = $('#boton_' + nombre_corte + '_PlusMinus')
  boton_PlusMinus.toggleClass('btn-primary');
  boton_PlusMinus.toggleClass('btn-default');
};


$(document).on('click', '.UpdateChartButton', function(){  

  $('#MensajeError').addClass('hidden');
  $("#SlideDisplaySection").removeAttr("style");
  $('#imagen_portada').addClass('hidden');
  $('#chart_lead').addClass('hidden');
  $('#unidades_denominador').addClass('hidden');
  $('#chart_units').addClass('hidden');
  $('#chart_div').addClass('hidden');
  $('#chart_loader').removeClass('hidden');

  var variable = $('#variable option:selected').val();
  var show_value_as = $('input:radio[name=show_value_as]:checked').val();

  var renglones = $('#CorteRenglones').val();
  var columnas = $('#CorteColumnas').val();

  var cortes = jQuery('.corte');
  var filtros = determinar_filtros(cortes);

  start_time = new Date()
  timer()
  
  $('.opciones_corte').addClass('hidden');
  $('.glyphicon_boton').removeClass('glyphicon-minus');
  $('.glyphicon_boton').addClass('glyphicon-plus');

  $.ajax({
    type: "POST",
    url: "/CNBVQueries",
    dataType: 'json',
    data: JSON.stringify({
      'data_requested': 'TestDataCNBV', 
      'variable': variable,
      'perspectiva_portafolio': $('input:radio[name=perspectiva_portafolio]:checked').val(),
      'perspectiva_institucion':$('input:radio[name=perspectiva_institucion]:checked').val(),
      'moneda':$('input:radio[name=moneda]:checked').val(),
      'show_value_as': show_value_as,
      'renglones':renglones,
      'columnas':columnas,
      'filtros':filtros
    })
  })
  .done(function(raw_data){
    $('#chart_loader').addClass('hidden');
    $('#chart_lead').removeClass('hidden');
    $('#unidades_denominador').removeClass('hidden');
    $('#chart_units').removeClass('hidden');
    $('#chart_div').removeClass('hidden');
    $('#boton_transponer').removeClass('hidden');
    $('#download_row').removeClass('hidden');    
    $('#chart_lead').text(raw_data['title']);
    chart_units = raw_data['chart_units'];
    
    chart_array = raw_data['chart_array'];

    if (chart_array.length == 2){
      // console.log('Si fue necesario transponer')
      chart_array = transpose_matrix(chart_array)
    }

    
    chart_type = $('input:radio[name=chart_type]:checked').val();
    denominador_actual = 1
    chart_array = divide_matrix(chart_array, $('#denominador').val())
    draw_chart(chart_array, chart_type)

    clearTimeout(t);
    seconds = 0; minutes = 0; hours = 0;  
    var milliseconds_since_start = new Date().valueOf() - start_time
    var m  = new Date(milliseconds_since_start)
    
    console.log('    ')
    console.log('Chart generado')
    console.log('Total de data points en query: ' + raw_data['total_dps'])
    console.log('Total de tiempo requerido para generar chart: '+m.getMinutes()+":"+m.getSeconds())
    console.log('    ')
    $('#chart_details_div').removeClass('hidden');
    $("#left_options_bar").animate({ scrollTop: 1000 }, "fast");
    $('#variable').popover('hide');
  })
});


// function draw_chart(chart_data, chart_type, chart_options, chart_details){
function draw_chart(chart_array, chart_type){
  // try{

    var unidades_denominador_locales = $('#denominador').find(':selected').attr('unidades_denominador');
    var chart_units_locales = chart_units

    var is_transposed = $('#is_transposed').is(':checked');
    if (is_transposed){
      chart_array = transpose_matrix(chart_array)
    }

    var is_sorted = $('#is_sorted').is(':checked');
    if (is_sorted){
      // console.log('Chart array antes de ordenar:')
      // console.log(chart_array)
      chart_array = SortChartArray(chart_array)
      // console.log()
      // console.log('Chart array despues de ordenar:')
      // console.log(chart_array)
    }

    if ( chart_type == 'column_chart' || chart_type == 'line_chart'){
        // console.log('Invirtiendo dentro de draw chart...')
        chart_array = invertir_renglones(chart_array)      
      }


    if ($('input:radio[name=show_value_as]:checked').val() == 'percentage'){
      axis_format = 'percent'
    } else {
      // axis_format = 'short'
      // axis_format = 'long'
      axis_format = 'decimal'
    }

    var as_delta = $('#as_delta').is(':checked');
    if (as_delta){
      chart_array = ShowAsPercentChange(chart_array)
      axis_format = 'percent'
      unidades_denominador_locales = ''
      chart_units_locales = 'Cambio porcentual v.s. el periodo anterior (%)'

    }

    var chart_data = google.visualization.arrayToDataTable(chart_array),
      options,
      axis_format,
      chart_subtitle, 
      chart;

    var is_donut = 0;
    if($('#is_donut').is(':checked')){
      is_donut = 0.4
    };

    var is_3D = $('#is_3D').is(':checked');
    
    var is_stacked = $('#is_stacked').is(':checked');
    var as_percent = $('#as_percent').is(':checked');
    if(is_stacked && as_percent){
      is_stacked = 'percent'
      axis_format = 'percent'
      unidades_denominador_locales = ''
      chart_units_locales = 'Como porcentaje del total (%)'
    }

    $('#unidades_denominador').text(unidades_denominador_locales);
    $('#chart_units').text(chart_units_locales);

    if ( chart_type == 'bar_chart'){

      options = {
        bar: { groupWidth: '80%'}, 
        chartArea:{height: '85%', width: '65%'},
        hAxis: {title:'', format: axis_format},
        isStacked: is_stacked      
      };

      chart = new google.visualization.BarChart(document.getElementById('chart_div'));

      chart_data = new google.visualization.DataView(chart_data);
      
      if($('#value_labels').is(':checked')){
        chart_data.setColumns([0, 1,
                           { calc: "stringify",
                             sourceColumn: 1,
                             type: "string",
                             role: "annotation" },
                           ]);
      }

      chart.draw(chart_data, options);

    } else if (chart_type == 'line_chart'){

      options = {      
        chartArea:{height: '75%', width: '87%'},
        legend: { position: 'top', maxLines:2},      
        vAxis: { format: axis_format}
        // curveType: 'function',
      };
      chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(chart_data, options);
    
    } else if(chart_type == 'column_chart') {
      options = {
        chartArea:{height: '75%', width: '87%'},
        legend: { position: 'top', maxLines:2},
        vAxis: { format: axis_format},
        isStacked: is_stacked
      };
      var view = new google.visualization.DataView(chart_data);
      // view.setColumns()
      chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(chart_data, options);
   
    } else if (chart_type == 'pie_chart'){

      options = {
        chartArea:{height: '85%', width: '85%'},
        // legend: { position: 'top', maxLines:2},
        pieHole: is_donut,
        legend: { position: 'right'},
        is3D: is_3D
        // title: ''
      };

      chart = new google.visualization.PieChart(document.getElementById('chart_div'));
      chart.draw(chart_data, options);

    };
    chart_url = chart.getImageURI()
    csvContent = "data:text/csv;charset=utf-8,";
    chart_array.forEach(function(infoArray, index){
       dataString = infoArray.join(",");
       csvContent += index < chart_array.length ? dataString+ "\n" : dataString;
    }); 
  // }
  // catch(err) {
  // var mensaje = 'No es posible generar una gráfica con las características seleccionadas. Por favor, modifica tu seleccón e inténtalo nuevamente'
  // MostrarMensajeError(mensaje)
  // }
};


function determinar_filtros(cortes){
  
  var filtros = {}; 
  var opciones_validas = [];

  cortes.each(function(){
    opciones = $(this).find('.opcion')
    
    opciones_validas = []

    opciones.each(function(){
      if ($(this).is(':checked')){
        opciones_validas.push($(this).val())
      };
    });
    filtros[$(this).attr("value")] = opciones_validas
  });
  return filtros;
}


function transpose_matrix(matrix){
  var newArray = [],
    origArrayLength = matrix.length,
    arrayLength = matrix[0].length,
    i;
  
  for(i = 0; i < arrayLength; i++){
      newArray.push([]);
  };

  for(i = 0; i < origArrayLength; i++){
      for(var j = 0; j < arrayLength; j++){
          newArray[j].push(matrix[i][j]);
      };
  };
  return newArray  
};


function invertir_renglones(matrix){

  var newArray = [matrix[0]],
    arrayLength = matrix.length,
    i;
  
  for(i = 1; i < arrayLength; i++){
      newArray.push(matrix[arrayLength - i]);
  };

  if($('#orden_matriz').val() == 'original'){
    $('#orden_matriz').val('invertido')
  } else {
    $('#orden_matriz').val('original')
  }

  return newArray  
};



//Oculta y muestra las etiquetas
$('input[type=radio][name=perspectiva_institucion]').on('change',function(){
  var perspectiva = $(this).val()
  
  if(perspectiva == 'varias_varios'){
    $('#value_labels').prop('checked', false)
    $('#value_labels_div').addClass('hidden')
  } else {
    $('#value_labels_div').removeClass('hidden')
  }
}); 


$('input[type=radio][name=chart_type]').on('change',function(){    
  
  if(chart_array != undefined){    
    chart_type = $('input:radio[name=chart_type]:checked').val();
    
    hide_group(opciones_visuales);
    unhide_group(menus_visibles[chart_type]);

    draw_chart(chart_array, chart_type);
  }
});  


$('#value_labels').on('change', function(){
  chart_type = $('input:radio[name=chart_type]:checked').val();  
  draw_chart(chart_array, chart_type);
});


$('.QuickChartViewUpdate').on('change', function(){
  chart_type = $('input:radio[name=chart_type]:checked').val();  
  draw_chart(chart_array, chart_type);
});


$(document).on('change', '.select_all_checkbox', function(){
  var checked_option = $(this).is(':checked')
  var target_section = $(this).attr('target_section');
  var opciones = $(target_section).find('.opcion');  

  opciones.each(function(){
    $(this).prop('checked', checked_option);
  });
});


$('input.opcion').on('change', function() {
  var nombre_corte = $(this).closest('#Corte').attr("value"),
    opciones_seleccionadas = $(this).closest('#Corte').find('.opcion').filter(':checked').length,
    limit;

  if (nombre_corte == 'institucion'){
    limit = limite_instituciones
  
  } else if(nombre_corte == 'periodo') {
    limit = limite_periodos
  
  } else {
    limit = 50
  }
  
   if(opciones_seleccionadas > limit) {
       this.checked = false;
   }
});


var grupo_totalBancaMultiple = [
  '#institucion_00'
]

var grupo_top7 = [
  '#institucion_16', //Banamex
  '#institucion_31', //Banorte/Ixe
  '#institucion_34', //BBVA Bancomer
  '#institucion_40', //HSBC
  '#institucion_42', //Inbursa
  '#institucion_53', //Santander
  '#institucion_55', //Scotiabank
]


var grupo_ultimoPeriodo = [
  '#periodo_201612'
]


var grupo_anos = [
  '#periodo_201612',
  '#periodo_201512',
  '#periodo_201412',
  '#periodo_201312',
  '#periodo_201212',
]



function select_group(lista_ids){
  
  var opciones = $(lista_ids[0]).closest('#Corte').find('.opcion');
  
  opciones.each(function(){
    $(this).prop('checked', false);
  });

  for( miembro in lista_ids){
    $(lista_ids[miembro]).prop('checked', true)
  }
};


function limpiar_corte(id_corte){
  var opciones = $(id_corte).find('.opcion');  
  opciones.each(function(){
    $(this).prop('checked', false);
  });
}


$('input[type=radio][name=perspectiva_institucion]').on('change',function(){
  var perspectiva = $('input:radio[name=perspectiva_institucion]:checked').val()

  if(perspectiva == 'varios_bancos'){
    select_group(grupo_ultimoPeriodo);
    select_group(grupo_top7);
    limite_periodos = 1;
    limite_instituciones = 7;
  
  } else if(perspectiva == 'varios_periodos'){
    select_group(grupo_anos);
    select_group(grupo_totalBancaMultiple);
    limite_periodos = 30;
    limite_instituciones = 1;
  
  } else if(perspectiva == 'varias_varios'){
    select_group(grupo_anos);
    select_group(grupo_top7);
    limite_periodos = 15;
    limite_instituciones = 7;

  }
});


var menus_visibles = {

  'siempre':['#boton_graficar', '#vista','#perspectiva_institucion', '[value=periodo]', '[value=institucion]'],

  'siempre_variable': {
    'concentracion_cartera':[ '#show_value_as'],
    'saldo_total':[ '#perspectiva_portafolio', '[value=tec]', '[value=estado]', '#tipo_de_grafica', '#opciones_visuales'],
  
    'car_vigente':['[value=tec]', '#tipo_de_grafica', '#opciones_visuales'],
    'car_vencida':['[value=tec]', '#tipo_de_grafica', '#opciones_visuales'],

    'creditos':['#perspectiva_portafolio', '[value=tec]', '[value=estado]', '#tipo_de_grafica', '#opciones_visuales'],
    'acreditados':['#perspectiva_portafolio', '[value=tec]', '[value=estado]', '#tipo_de_grafica', '#opciones_visuales'],
    
    'plazo':['#perspectiva_portafolio', '[value=tec]', '#tipo_de_grafica', '#opciones_visuales', '#tipo_moneda'],
    'tasa':['#perspectiva_portafolio', '[value=tec]',  '#tipo_de_grafica', '#opciones_visuales', '#tipo_moneda'],

    'imor':['#tipo_de_grafica', '#opciones_visuales'] 
  },

  'total':{
    'concentracion_cartera':[],
    'saldo_total':['[value=destino]', '[value=monto]', '[value=garantia]', '[value=calificacion]', '[value=sector]'],
  
    'car_vigente':[],
    'car_vencida':[],

    'creditos':['[value=monto]', '[value=garantia]', '[value=calificacion]', '[value=sector]'],
    'acreditados':['[value=sector]'],
    
    'plazo':['[value=destino]', '[value=monto]', '[value=sector]'],
    'tasa':['[value=destino]', '[value=monto]', '[value=garantia]', '[value=calificacion]', '[value=sector]'],

    'imor':['[value=monto]', '[value=garantia]', '[value=calificacion]', '[value=estado]', '[value=sector]'],
  },

  'marginal':{
    'concentracion_cartera':[],
    'saldo_total':['[value=intervalo]', '[value=moneda]'],
  
    'car_vigente':[],
    'car_vencida':[],

    'creditos':['[value=intervalo]', '[value=moneda]'],
    'acreditados':[],
    
    'plazo':[],
    'tasa':['[value=intervalo]'],

    'imor':[],
  },

 'bar_chart':[
    '#is_transposed_col',
    '#is_sorted_col',
    '#is_stacked_col',
    '#value_labels_div',
    
    '#as_delta_col',
    '#as_percent_col',
    '#denominador_col'
  ],

  'pie_chart': [
    '#is_transposed_col',
    '#is_sorted_col',
    
    '#is_donut_col',
    '#is_3D_col',
    
    '#denominador_col'
  ],
  
  'line_chart': [
    '#is_transposed_col',
    '#denominador_col'
  ],
  
  'column_chart': [
    '#is_transposed_col',
    '#is_sorted_col',
    '#is_stacked_col',
    '#as_delta_col',
    '#as_percent_col',
    '#denominador_col'
  ]
}

var opciones_visuales = [
  '#is_transposed_col',
  '#is_sorted_col',
  '#is_stacked_col',
  '#value_labels_div',
  '#is_donut_col',
  '#is_3D_col',
  '#as_delta_col',
  '#as_percent_col',
  '#denominador_col'
]


var cortes_incompatibles = {
  'periodo':[],
  'institucion':[],
  'estado':['moneda', 'estado', 'destino', 'intervalo', 'monto', 'garantia', 'calificacion', 'sector'],
  'tec':['intervalo', 'monto', 'moneda', 'garantia', 'calificacion', 'sector'],
  'intervalo':['tec', 'estado', 'destino', 'garantia', 'calificacion', 'sector'],
  'monto': ['tec', 'estado', 'destino', 'garantia', 'calificacion', 'sector'],
  'moneda':['estado', 'tec', 'monto', 'garantia', 'calificacion', 'sector'],
  'destino':['estado', 'intervalo', 'monto', 'garantia', 'calificacion', 'sector'],
  'garantia':['estado', 'tec', 'intervalo', 'monto', 'moneda', 'destino', 'calificacion', 'sector'],
  'calificacion':['estado', 'tec', 'intervalo', 'monto', 'moneda', 'destino', 'garantia', 'sector'],
  'sector': ['estado', 'tec', 'intervalo', 'monto', 'moneda', 'destino', 'garantia', 'calificacion']
}




function validar_compatibilidad(corte_seleccionado, corte_activo){

  $('.SeleccionarCorte').popover('hide');
  if(jQuery.inArray(corte_seleccionado.val(), cortes_incompatibles[corte_activo.val()]) == -1  ){      
    $('.SeleccionarCorte').popover('hide');
    return true

  } else {
    corte_activo = boton_corte = $('#boton_' + corte_activo.val())   
    var popover_content = 'No será posible mostrar información para la combinacion de vistas: ' + corte_seleccionado.text() + ' y ' + corte_activo.text() +'. Por favor, modifique su selección';    
    corte_seleccionado.attr('data-content', popover_content);    
    corte_seleccionado.popover('show');
    return false
  }  
};


var to_be_hidden = [
  '#show_value_as',
  '#perspectiva_institucion',
  '#perspectiva_portafolio',
  '#vista', 
  '[value=periodo]', 
  '[value=institucion]', 
  '[value=tec]', 
  '[value=estado]',
  '[value=intervalo]',
  '[value=monto]',  
  '#tipo_de_grafica',
  '#boton_graficar',
  '#tipo_moneda',
  '[value=moneda]',
  '[value=destino]',
  '[value=garantia]',
  '[value=calificacion]',
  '[value=sector]',
]


var seleccion_default = {

  'saldo_total':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'creditos':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'acreditados':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'car_vigente':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },
  
  'car_vencida':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'tasa_i_mn':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'tasa_i_me':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'tasa_i_udis':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'plazo_ponderado':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },

  'concentracion_cartera':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'line_chart'
  },

  'tasa':{
    'periodos': ['#periodo_201612'],
    'instituciones': grupo_top7,
    'corte_renglones':'institucion',
    'corte_columnas': 'tec',
    'grafica': 'bar_chart'
  },

  'plazo':{
    'periodos': ['#periodo_201610'],
    'instituciones': grupo_top7,
    'corte_renglones':'institucion',
    'corte_columnas': 'tec',
    'grafica': 'bar_chart'
  },

  'imor':{
    'periodos': grupo_ultimoPeriodo,
    'instituciones': grupo_top7,
    'corte_renglones':'periodo',
    'corte_columnas': 'institucion',
    'grafica': 'bar_chart'
  },
}


function seleccionar_cortes_iniciales(CorteRenglones, CorteColumnas){

  var cortes = jQuery('.corte');
  
  cortes.each(function(){
    var boton_corte = $(this).find('.SeleccionarCorte')[0]

    $(boton_corte).find('#OkGlyphicon').addClass('hidden'); 
    $(boton_corte).removeClass('btn-primary');
    $(boton_corte).addClass('btn-default');
    $(boton_corte).attr("corte_activo", "No");

    var boton_PlusMinus = $(this).find('.ExpandColapseSection')[0]
    $(boton_PlusMinus).removeClass('btn-primary');
    $(boton_PlusMinus).addClass('btn-default');

  });

  if (CorteRenglones){
    $('#CorteRenglones').val(CorteRenglones)
    flipear_boton_corte(CorteRenglones);
  }

  if (CorteColumnas){
    $('#CorteColumnas').val(CorteColumnas);
    flipear_boton_corte(CorteColumnas);
  }
}


function seleccionar_grafica_inicial(chart_type){  
  $('input:radio[name=chart_type]').attr('checked',false)
  // console.log('Si se dio cuenta de que deberia de seleccionar la grafica de tipo: ' + chart_type)
  $('input[type=radio][name=chart_type][value=' + chart_type +']' ).prop('checked', true)
};




function unhide_group(lista_ids){
  for( miembro in lista_ids){
    $(lista_ids[miembro]).removeClass('hidden') 
  }
};


function hide_group(lista_ids){
  for( miembro in lista_ids){
    $(lista_ids[miembro]).addClass('hidden') 
  }
};


function seleccionar_default(variable){

  var seleccion_inicial = seleccion_default[variable]
  select_group(seleccion_inicial['periodos']);
  select_group(seleccion_inicial['instituciones']);
  seleccionar_cortes_iniciales(seleccion_inicial['corte_renglones'], seleccion_inicial['corte_columnas']);
  seleccionar_grafica_inicial(seleccion_inicial['grafica']);

}; 

$('#variable').on('change', function(){

  hide_group(to_be_hidden);
  var variable = $(this).val();  
  var grupo_visible = menus_visibles['siempre'].concat(menus_visibles['siempre_variable'][variable], menus_visibles[$('input:radio[name=perspectiva_portafolio]:checked').val()][variable]);
  // console.log(' ')
  // console.log('Este es el grupo de menus visibles')
  // console.log(grupo_visible)

  var popover_content;

  if( variable == 'tasa' || variable == 'plazo'){
    popover_content = "Para que los valores graficados de ésta variable sean correctos, es necesario siempre seleccionar la vista 'Banco' y una más que no sea 'Periodo'" 
    $('#variable').attr('data-content', popover_content);  
    $('#variable').popover('show');
  
  } else if(variable == 'imor'){
    popover_content = "Para que los valores graficados de ésta variable sean correctos, es necesario siempre seleccionar la vista 'Banco'" 
    $('#variable').attr('data-content', popover_content);
    $('#variable').popover('show');
  
  }else {
    $('#variable').popover('hide');
  }

  
  unhide_group(grupo_visible);
  seleccionar_default(variable);
});

$('#perspectiva_portafolio').on('change',function(){
  var variable = $('#variable').val();  
  var perspectiva_portafolio = $('input:radio[name=perspectiva_portafolio]:checked').val();
  var menus_total = menus_visibles['total'][variable];
  var menus_marginal = menus_visibles['marginal'][variable];

  if ( perspectiva_portafolio == 'total'){
    hide_group(menus_marginal);
    unhide_group(menus_total);
  } else {
    hide_group(menus_total);
    unhide_group(menus_marginal);
  }
});


$('#denominador').on('change', function(){  
  var denominador = $(this).val();  
  chart_array = divide_matrix(chart_array, denominador)
  chart_type = $('input:radio[name=chart_type]:checked').val();  
  $('#unidades_denominador').text($(this).find(':selected').attr('unidades_denominador'));

  draw_chart(chart_array, chart_type);
});


function divide_matrix(matrix, denominador){
  
  var newArray = [matrix[0]],
    renglonesMatriz = matrix.length,
    columnasMatriz = matrix[0].length,
    k,
    i;
 
  for(k = 1; k < renglonesMatriz; k++){
      newArray.push([matrix[k][0]]);
  };
  
  for(i = 1; i < renglonesMatriz; i++){
      for(var j = 1; j < columnasMatriz; j++){
          // newArray[i].push(matrix[i][j]/parseInt(denominador)*denominador_actual);
          newArray[i].push(parseFloat((matrix[i][j]/parseInt(denominador)*denominador_actual).toFixed(2)));
          // console.log(parseFloat((matrix[i][j]/parseInt(denominador)*denominador_actual).toFixed(2)));
      };
  };

  denominador_actual = denominador

  return newArray

};



function SumChartRow(chart_row){
  var row_total = 0
  for (var i = chart_row.length - 1; i > 0; i--) {
    row_total += chart_row[i]
  }
  return row_total
};


function SortChartArray(chart_array){
    
  var old_array = chart_array.slice()
  var sorted_array = [old_array.shift()]

  old_array.sort(function (a, b) {    
    return SumChartRow(b) - SumChartRow(a);
  });

  return sorted_array.concat(old_array)
}


function MostrarMensajeError(mensaje){
  $('#chart_loader').addClass('hidden');
  $('#chart_lead').addClass('hidden');
  $('#unidades_denominador').addClass('hidden');
  $('#chart_units').addClass('hidden');
  $('#chart_div').addClass('hidden');
  
  $('#MensajeError').removeClass('hidden');
  $('#TextoMensajeError').text(mensaje)

  clearTimeout(t);
  seconds = 0; minutes = 0; hours = 0;  
};


$( document ).ajaxError(function(){
  var mensaje = 'Hubo un problema al intentar obtener los datos para generar la gráfica según los campos seleccionados. <br><br> Por favor, modifica tu seleccón e inténtalo nuevamente'
  MostrarMensajeError(mensaje)
});


$('#download_button').on('click', function(){
  var link = document.createElement('a');
    link.href = chart_url;
    link.download = 'Gráfica_CNBV.png';
    document.body.appendChild(link);
    link.click(); 
});


$('#download_datos').on('click', function(){
  var encodedUri = encodeURI(csvContent);
  var link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", "Datos_CNBV.csv");
  document.body.appendChild(link); // Required for FF
  link.click();
});



function CalcRowChange(chart_row){
  var new_row = []

  for (var i = chart_row.length - 1; i > 1; i--) {
    var valor = chart_row[i-1]/chart_row[i]-1;
    if ($.isNumeric(valor)){
      new_row.unshift(valor)
    } else {
      new_row.unshift(0)
    }     
  }
  new_row.unshift(chart_row[0])   
  return new_row
};


function ShowAsPercentChange(chart_array){
  // var base_array = chart_array.slice()
  var base_array = JSON.parse(JSON.stringify(chart_array))

  // console.log('El array al entrar')
  // console.log(chart_array)
  base_array[0].pop()
  // console.log('El array al salir')
  // console.log(chart_array) 

  var new_array = [base_array.shift()]
  
  for (var i = 0; i <= base_array.length - 1; i++) {
    new_array.push(CalcRowChange(base_array[i])) 
  }

  return new_array
};



