import {createI18n} from 'vue-i18n'

export const messages = {
    en: {},
    fr: {},
}


export default createI18n({
    legacy: false,
    locale: 'fr',
    fallbackLocale: 'fr',
    messages
})
