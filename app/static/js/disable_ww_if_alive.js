$(document).ready(function() {
    $('input:radio[name="jon_snow"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="jon_snow_ww"]').prop("checked", false);
            $('input:checkbox[name="jon_snow_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="jon_snow_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="sansa_stark"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="sansa_stark"]').prop("checked", false);
            $('input:checkbox[name="sansa_stark_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="sansa_stark_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="arya_stark"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="arya_stark_ww"]').prop("checked", false);
            $('input:checkbox[name="arya_stark_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="arya_stark_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="bran_stark"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="bran_stark_ww"]').prop("checked", false);
            $('input:checkbox[name="bran_stark_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="bran_stark_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="cersei_lannister"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="cersei_lannister_ww"]').prop("checked", false);
            $('input:checkbox[name="cersei_lannister_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="cersei_lannister_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="jamie_lannister"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="jamie_lannister_ww"]').prop("checked", false);
            $('input:checkbox[name="jamie_lannister_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="jamie_lannister_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="tyrion_lannister"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="tyrion_lannister_ww"]').prop("checked", false);
            $('input:checkbox[name="tyrion_lannister_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="tyrion_lannister_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="daenerys_targaryen"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="daenerys_targaryen_ww"]').prop("checked", false);
            $('input:checkbox[name="daenerys_targaryen_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="daenerys_targaryen_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="theon_greyjoy"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="theon_greyjoy_ww"]').prop("checked", false);
            $('input:checkbox[name="theon_greyjoy_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="theon_greyjoy_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="yara_greyjoy"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="yara_greyjoy_ww"]').prop("checked", false);
            $('input:checkbox[name="yara_greyjoy_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="yara_greyjoy_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="melisandre"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="melisandre_ww"]').prop("checked", false);
            $('input:checkbox[name="melisandre_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="melisandre_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="jorah_mormont"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="jorah_mormont_ww"]').prop("checked", false);
            $('input:checkbox[name="jorah_mormont_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="jorah_mormont_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="the_hound"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="the_hound_ww"]').prop("checked", false);
            $('input:checkbox[name="the_hound_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="the_hound_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="the_mountain"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="the_mountain_ww"]').prop("checked", false);
            $('input:checkbox[name="the_mountain_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="the_mountain_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="samwell_tarly"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="samwell_tarly_ww"]').prop("checked", false);
            $('input:checkbox[name="samwell_tarly_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="samwell_tarly_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="gilly"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="gilly_ww"]').prop("checked", false);
            $('input:checkbox[name="gilly_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="gilly_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="sam_jr"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="sam_jr_ww"]').prop("checked", false);
            $('input:checkbox[name="sam_jr_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="sam_jr_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="lord_varys"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="lord_varys_ww"]').prop("checked", false);
            $('input:checkbox[name="lord_varys_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="lord_varys_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="brienne_of_tarth"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="brienne_of_tarth_ww"]').prop("checked", false);
            $('input:checkbox[name="brienne_of_tarth_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="brienne_of_tarth_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="davos_seaworth"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="davos_seaworth_ww"]').prop("checked", false);
            $('input:checkbox[name="davos_seaworth_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="davos_seaworth_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="bronn"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="bronn_ww"]').prop("checked", false);
            $('input:checkbox[name="bronn_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="bronn_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="podrick_payne"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="podrick_payne_ww"]').prop("checked", false);
            $('input:checkbox[name="podrick_payne_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="podrick_payne_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="tormund_giantsbane"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="tormund_giantsbane_ww"]').prop("checked", false);
            $('input:checkbox[name="tormund_giantsbane_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="tormund_giantsbane_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="greyworm"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="greyworm_ww"]').prop("checked", false);
            $('input:checkbox[name="greyworm_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="greyworm_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="gendry"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="gendry_ww"]').prop("checked", false);
            $('input:checkbox[name="gendry_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="gendry_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="beric_dondarrion"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="beric_dondarrion_ww"]').prop("checked", false);
            $('input:checkbox[name="beric_dondarrion_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="beric_dondarrion_ww"]').attr("disabled", false);
        }
    });

    $('input:radio[name="euron_greyjoy"]').change(function() {
        if ($(this).val() === 'Alive') {
            $('input:checkbox[name="euron_greyjoy_ww"]').prop("checked", false);
            $('input:checkbox[name="euron_greyjoy_ww"]').attr("disabled", true);
        }
        else {
            $('input:checkbox[name="euron_greyjoy_ww"]').attr("disabled", false);
        }
    });
});
