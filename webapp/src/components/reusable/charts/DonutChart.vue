<template>
  <div id="donut-chart"></div>
</template>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import ApexCharts from "apexcharts"

const props = defineProps<{
  data: number[] | undefined
  labels: string[] | undefined
}>()

let chart: ApexCharts | null = null

const renderChart = () => {
  const options: ApexCharts.ApexOptions = {
    series: props.data,
    chart: {
      events: {
        click: undefined,
      },
      height: "100%",
      width: "100%",
      type: "donut",
    },
    colors: ["#002665", "#9FD0F0"],
    labels: props.labels,
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
      custom: function ({ series, seriesIndex, w }) {
        const data = series[seriesIndex]
        const label = w.globals.labels[seriesIndex]
        return `
          <div class="p-1.5 shadow rounded bg-black/80 text-white text-xs text-wrap w-24 max-w-24 text-center">
            <strong>${label}</strong>: ${data.toLocaleString("fr-BE", {
          maximumFractionDigits: 2,
        })}
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
              offsetY: 20,
              formatter: () => "> LOQ",
            },
            value: {
              show: true,
              fontSize: "20px",
              fontWeight: 500,
              color: "#002665",
              offsetY: -20,
              formatter: (value: string) =>
                parseInt(value)
                  .toLocaleString("fr-BE", { maximumFractionDigits: 2 })
                  .toString(),
            },

            total: {
              show: true,
              showAlways: true,
              color: "#002665",
              fontWeight: 600,
              formatter: (w) => {
                const total = w.globals.seriesTotals.reduce(
                  (a: number, b: number) => a + b,
                  0
                )
                const aboveLOQ = w.globals.series[1]
                return `${((aboveLOQ / total) * 100).toLocaleString("fr-BE", {
                  maximumFractionDigits: 2,
                })}%`
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

  if (chart) {
    chart.destroy()
  }

  const donutChartElement = document.getElementById("donut-chart")
  if (donutChartElement && typeof ApexCharts !== "undefined") {
    chart = new ApexCharts(donutChartElement, options)
    chart.render()
  }
}

onMounted(() => {
  renderChart()
})

watch([() => props.data, () => props.labels], renderChart)
</script>
