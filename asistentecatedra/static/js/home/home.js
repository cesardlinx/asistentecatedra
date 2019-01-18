$(document).ready(function() {

    // Animaciones Home
    var scrollCurriculum = true;
    var scrollDispositivos = true;
    var scrollExporting = true;

    $(window).on('scroll', function() {
        var winHeightAnim = $(window).height();

        winHeightAnim = winHeightAnim * (2 / 3);

        var curriculumSection = document.getElementById('curriculum');
        var dispositivosSection = document.getElementById('dispositivos');
        var exportingSection = document.getElementById('exporting');

        var curriculumHeight = curriculumSection.getBoundingClientRect().top;
        var dispositivosHeight = dispositivosSection.getBoundingClientRect().top;
        var exportingHeight = exportingSection.getBoundingClientRect().top;

        // Animacion Curriculum
        if ((curriculumHeight < winHeightAnim) && scrollCurriculum === true) {
            scrollCurriculum == false;
            $('#curriculum .titulo-secundario').addClass('slide-up-fast');
            $('#curriculum p').addClass('slide-up-slow');
        }

        // Animacion Dispositivos
        if ((dispositivosHeight < winHeightAnim) && scrollDispositivos === true) {
            scrollDispositivos == false;
            $('#dispositivos .dispositivos-img').addClass('fade-in');
            $('#dispositivos .titulo-secundario').addClass('enter-right-fast');
            $('#dispositivos p').addClass('enter-right-slow');
        }

        // Animacion Exportación
        if ((exportingHeight < winHeightAnim) && scrollExporting === true) {
            scrollExporting == false;
            $('#exporting .exporting-img').addClass('slide-up-xslow');
            $('#exporting .titulo-secundario').addClass('enter-left-fast');
            $('#exporting p').addClass('enter-left-slow');
        }
    });
});