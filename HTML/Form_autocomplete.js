//FORMULARIO AUTOCOMPLETAR
$(function() {
    var availableTags = [
	"Álgebra Lineal",
	"Cálculo I",
	"Mecánica Fundamental",
	"Química I",
	"Fundamentos de Informática",
	"Geometría",
	"Cálculo II",
	"Termodinámica Fundamental",
	"Química II",
	"Expresión Gráfica",
	"Electromagnetismo",
	"Métodos Numéricos",
	"Materiales",
	"Economía y Empresa",
	"Estadística",
	"Dinámica de Sistemas",
	"Proyecto I",
	"Tecnología del Medio Ambiente y Sostenibilidad",
	"Termodinámica",
	"Electrotecnia",
	"Mecánica de los Medios Continuos",
	"Técnicas Estadísticas para la Calidad",
	"Mecánica de Fluidos",
	"Organización y Gestión",
	"Resistencia de Materiales",
	"Proyecto II",
	"Gestión de Proyectos",
	"Electrónica",
	"Sistemas de Fabricación",
	"Ecuaciones Diferenciales",
	"Informática",
	"Mecánica",
	"Teoría de Máquinas y Mecanismos",
	"Tecnología y Selección de Materiales",
	"Máquinas Eléctricas",
	"Optimización y Simulación",
	"Termotecnia",
	"Control Automático",
	"Ampliación de Mecánica",
	"Comunicación de Información Técnica",
	"Debates Sobre Tecnología y Sociedad",
	"Los Orígenes de la Ingeniería Moderna",
	"Juegos para Computadores. Estructura y Desarrollo",
	"Taller Eléctrico",
	"Tecnología de la Luz",
	"Tecnologías Digitales para la Comunicación de los Proyectos",
	"Historia de la Ingeniería Industrial. La Escuela de Barcelona",
	"Ampliación de Química",
	"Rehabilitación y Eficiencia Energética en la Edificación",
	"Movilidad Eléctrica",
	"Desarrollo de Aplicaciones Basadas en Microcontroladores",
	"Taller Electrónico",
	"Sistemas Mecánicos",
	"Vehículos",
	"Desarrollo Tecnológico y Científico en la Antigüedad. Egipto y Oriente Próximo",
	"Análisis de Datos para la Industria y los Servicios",
	"Fusión Nuclear. Iter",
	"Logística Control de Flotas y Sig",
	"La Historia de la Matemática Aplicada en la Ingeniería",
	"Albert Einstein y la Ciencia y la Técnica del Siglo XX",
	"Cultura Tecnología e Historia en China y Japón",
	"Ingeniería Industria y Sociedad",
	"Dinámica Computacional de Fluidos",
	"Sistemas de Distribución de Tuberías",
	"Sistemas de Gestión",
	"Ampliación de Resistencia de Materiales",
	"Análisis de Componentes Estructurales y Mecánicos para el MEF",
	"La Robótica en la Ingeniería",
	"Tecnología Ferroviaria",
	"Polímeros en la Industria",
	"Técnicas de Ensayos No Destructivos Industriales",
	"Comunicación Oral en Inglés Académico y Profesional"
    ];
    function split( val ) {
	return val.split( /,\s*/ );
    }
    function extractLast( term ) {
	return split( term ).pop();
    }

    $( "#tags" )
    // don't navigate away from the field on tab when selecting an item
	.bind( "keydown", function( event ) {
	    if ( event.keyCode === $.ui.keyCode.TAB &&
		 $( this ).autocomplete( "instance" ).menu.active ) {
		event.preventDefault();
	    }
	})
	.autocomplete({
	    minLength: 0,
	    source: function( request, response ) {
		// delegate back to autocomplete, but extract the last term
		response( $.ui.autocomplete.filter(
		    availableTags, extractLast( request.term ) ) );
	    },
	    focus: function() {
		// prevent value inserted on focus
		return false;
	    },
	    select: function( event, ui ) {
		var terms = split( this.value );
		// remove the current input
		terms.pop();
		// add the selected item
		terms.push( ui.item.value );
		// add placeholder to get the comma-and-space at the end
		terms.push( "" );
		this.value = terms.join( ", " );
		return false;
	    }
	});
});
