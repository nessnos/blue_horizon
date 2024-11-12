import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HelloWorld.vue"),
    },
  ],
})

router.afterEach((to) => {
  if (to.hash) {
    const element = document.querySelector(to.hash) as HTMLElement
    if (element) {
      element.scrollIntoView({ behavior: "smooth" })
    }
  }
})

export default router
