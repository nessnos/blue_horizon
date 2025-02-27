<template>
  <div id="donut-chart"></div>
</template>
<script lang="ts" setup>
import { onMounted } from "vue"
import ApexCharts from "apexcharts"
import type { BarData } from "@/type"

defineProps<{
  chartData: BarData[]
}>()

const series = [44, 55]

onMounted(() => {
  const options: ApexCharts.ApexOptions = {
    series: series,
    chart: {
      events: {
        click: undefined,
      },
      height: "100%",
      width: "100%",
      type: "donut",
      offsetX: 50,
    },
    colors: ["#002665", "#9FD0F0"],
    labels: ["Under LOQ", "Above LOQ"],
    legend: {
      show: false,
    },
    stroke: {
      show: false,
    },
    dataLabels: {
      enabled: false,
    },
    tooltip: {
      custom: function ({ series, seriesIndex }) {
        const data = series[seriesIndex]
        return `
          <div class="p-1.5 shadow rounded bg-black/80 text-white text-xs">
            ${data}%
          </div>
        `
      },
    },
    plotOptions: {
      pie: {
        startAngle: 10,
        expandOnClick: false,
        donut: {
          size: "85%",
          labels: {
            show: true,
            name: {
              show: true,
              offsetY: 15,
              formatter: () => "above LOQ",
            },
            value: {
              show: true,
              fontSize: "20px",
              fontWeight: 500,
              color: "#002665",
              offsetY: -25,
            },

            total: {
              show: true,
              showAlways: true,
              color: "#002665",
              fontWeight: 600,
              formatter: (w) => {
                const total = w.globals.seriesTotals.reduce(
                  (a: number, b: number) => b,
                  0
                )
                return `${total}%`
              },
            },
          },
        },
      },
    },
    states: {
      hover: {
        filter: {
          type: "darken",
        },
      },
    },
  }

  const donutChartElement = document.getElementById("donut-chart")
  if (donutChartElement && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(donutChartElement, options)
    chart.render()
  }
})
</script>
