import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/map",
      name: "map",
      component: () => import("../views/MapView.vue"),
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: () => import("../views/DashboardView.vue"),
    },
    {
      path: "/machine-learning",
      name: "machine-learning",
      component: () => import("../views/MachineLearningView.vue"),
    },
    {
      path: "/machine-learning/details/pipeline",
      name: "pipeline-details",
      component: () => import("../views/PipelineDetailsView.vue"),
    },
    {
      path: "/chat",
      name: "chat",
      component: () => import("../views/ChatView.vue"),
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
