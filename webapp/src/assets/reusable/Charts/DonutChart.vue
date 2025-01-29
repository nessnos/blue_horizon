<template>
    <div id="donut-chart"></div>
    </template>
    <script setup lang="ts">
    import { onMounted } from 'vue';
    import ApexCharts from 'apexcharts'
    import type { BarData } from '@/type' ;
    
    const props = defineProps<{
      chartData: BarData[];
      }>();

      onMounted(() => {
  const options: ApexCharts.ApexOptions = {
    series: [44, 55],
    chart: {
      height: "100%",
      width: "100%",
      type: 'donut',
      offsetX: 50
    },
    colors : ['#002665', '#9fd0f0'],
    labels: ['Under LOQ', 'Above LOQ'],
    legend: {
      show: false,
    },
    stroke: {
      show: false,
    },
    dataLabels: {
      enabled: false
    },
    plotOptions: {
      pie: {
        startAngle: 10,
        donut: {
          size: '85%',
          labels: {
            show: true,
            name: {
              show: true,
              offsetY: 15,
              formatter: () => 'above LOQ'
            },
            value: {
              show: true,
              fontSize: '20px',
              fontWeight: 500,
              color: '#002665',
              offsetY: -25
            },
            total: {
              show: true,
              showAlways: true,
              color: '#002665',
              fontWeight: 600,
              formatter: (w) => {
                const total = w.globals.seriesTotals.reduce(
                  (a, b) => b,
                  0
                );
                return `${total}%`;
              }
            }
          }
        },
      },
    },
  };

  const donutChartElement = document.getElementById("donut-chart");
  if (donutChartElement && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(donutChartElement, options);
    chart.render();
  }
});
    </script>
  