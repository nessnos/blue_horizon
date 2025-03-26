import "./assets/main.scss"

import { createApp } from "vue"
import { createPinia } from "pinia"
import i18n from "@/i18n"
import axios from "axios"
import "/node_modules/flag-icons/css/flag-icons.min.css"

import App from "./App.vue"
import router from "./router"

const app = createApp(App)

axios.defaults.baseURL = "http://127.0.0.1:8000"

app.config.globalProperties.$axios = axios

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount("#app")
