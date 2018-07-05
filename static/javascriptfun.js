$(document).ready( function(){
  // ENSENIARLE A LAS TARJETAS QUE CUANDO LES HAGAN CLICK, SE MARQUEN SELECCIONADAS
  $("#changeButton").click( function(){
    document.getElementById('ciaoOrHola').innerHTML = 'Hola!';
    document.getElementById('ciaoOrHola').className = 'color-red';

  } );

  $('#seleccionarTodas').change( function(){
    console.log($(this).is(":checked"));
  } )

} );
