<template>
    <div class="px-2 pt-4" id="donut-chart"></div>
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
    },
    labels: ['Under LOQ', 'Above LOQ'],
    legend: {
      show: false,
    },
    stroke: {
      show: false,
    },
    plotOptions: {
      pie: {
        donut: {
          labels: {
            show: true,
            name: {
              show: false,
            },
            value: {
              show: true,
              fontSize: '24px',
              fontWeight : 900,
              color: undefined,
              offsetY: 24,
              formatter: (val: string): string => {
                return val;
              },
            },
            total: {
              show: true,
              label: '',
              color: '#373d3f',
              formatter: (w: any): string => {
                return w.globals.seriesTotals.reduce((a: number, b: number) => {
                  return a + b;
                }, 0);
              },
            },
          },
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
  