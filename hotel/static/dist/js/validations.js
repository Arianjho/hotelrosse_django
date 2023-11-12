$(document).ready(function () {
    'use strict';

    var OptionsBase = {
        errorElement: "div",
        errorClass: "invalid-feedback",
        validClass: "is-valid",
        errorPlacement: function (error, element) {
            error.addClass("invalid-feedback");
            error.insertAfter(element);
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass('is-invalid').removeClass(validClass);
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).addClass(validClass).removeClass('is-invalid');
        }
    };

    $("#form_agregar_habitacion").validate($.extend({}, OptionsBase, {
        rules: {
            habitacion: {
                required: true
            },
            tipo: {
                required: true
            }
        },
        messages: {
            habitacion: {
                required: "Por favor, ingrese el n° de habitacion."
            },
            tipo: {
                required: "Por favor, seleccione el tipo de habitacion."
            }
        }
    }));

    $("#form_agregar_huesped").validate($.extend({}, OptionsBase, {
        rules: {
            dni: {
                required: true,
                minlength: 8,
                maxlength: 8,
                digits: true
            },
            huesped: {
                required: true
            }
        },
        messages: {
            dni: {
                required: "Por favor, ingrese el DNI.",
                minlength: "El DNI debe tener exactamente 8 dígitos.",
                maxlength: "El DNI debe tener exactamente 8 dígitos.",
                digits: "El DNI solo debe contener dígitos."
            },
            huesped: {
                required: "Por favor, ingrese el nombre del huésped."
            }
        },
        errorPlacement: function(error, element) {
            if (element.attr("name") == "dni") {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }
    }));
    
});