'use strict';
/* AGREGO PARA DESHABILITAR BOTON DE GUARDADO UNA VEZ QUE SE PRESIONA */
{
    const inputTags = ['BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'];
    const modelName = document.getElementById('django-admin-form-add-constants').dataset.modelName;
    if (modelName) {
        const form = document.getElementById(modelName + '_form');
        const saveButton = document.querySelector('input[type="submit"][name="_save"]');
        for (const element of form.elements) {
            // HTMLElement.offsetParent returns null when the element is not
            // rendered.
            if (inputTags.includes(element.tagName) && !element.disabled && element.offsetParent) {
                element.focus();
                break;
            }
        }

        if (saveButton) {
            form.addEventListener('submit', function() {
                saveButton.setAttribute('disabled', 'disabled');
            });
        }

    }
}
