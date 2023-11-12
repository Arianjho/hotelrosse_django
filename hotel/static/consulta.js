$(document).ready(function () {
    'use strict';

    function toTitleCase(str) {
        return str.toLowerCase().split(' ').map(function(word) {
            return word.charAt(0).toUpperCase() + word.slice(1);
        }).join(' ');
    }
    
    $('#consultar_dni').on('click', function () {
    
        var dni = $('#dni').val();
        $('#consultar_dni').prop('disabled', true);
    
        $.ajax({
            url: "/consultar_dni/"+dni+"/",
            type: "GET",
            dataType: "json",
            success: function(data) {
    
                var nombre_uppercase = `${data.nombres} ${data.apellidoPaterno} ${data.apellidoMaterno}`;
                var nombre_oration = toTitleCase(nombre_uppercase);
    
                $('#huesped').val(nombre_oration);
                $('#consultar_dni').prop('disabled', false);
            },
            error: function(error) {
                $('#consultar_dni').prop('disabled', false);
            }
        });
    });
});