export interface Country {
  name: string,
  code: string,
  clicked: boolean
}

export interface CountryGeneralInfo {
  [label: string]: string | number;
}

export interface Option {
  name: string,
  start?: string,
  end?: string
  code?: string,
}

export interface DashboardData {
  count_chemicals_monitored: number;
  count_monitoring_sites: number;
  number_of_collected_samples: number;
  proportion_of_confirmed_samples: number;
  loq_donut: {
    data: number[];
    labels: string[];
  };
  property_line: { x: string; y: number }[];
  property_bar: { x: string; y: number }[];
  determinand_table: {
    determinand: string;
    total_samples: number;
    mean: number;
    min: number;
    max: number;
    count_below_loq: number;
  }[];
  waterbody_table : [
    {
      category : string,
      number : number
    }
  ]
}

export interface FilterType {
  country?: string;
  reference_year__range?: [string, string] | string;
  observed_property_determinand?: string;
  matrix?: string;
}

export interface ChartData {
  x: string | number,
  y: number,
}

export interface ModelParameter {
  value: number | boolean | string;
  type: "slider" | "checkbox";
  label: string;
  min?: number;
  max?: number;
  step?: number;
}

export interface Model {
  name: string;
  technical_name : string;
  parameters?: Record<string, ModelParameter>;
}

export interface Pipeline {
  id : string, 
  task_id : string, 
  status : string, 
  model_name : string,
  started_at : string, 
  completed_at : string, 
  results : PipelineResult
}


export interface Metrics {
  mean_absolute_error: number;
  mean_squared_error: number;
  root_mean_squared_error: number;
  r_squared? : number;
}

export interface SeriesData {
  x: number | string;
  y: number;
}

export interface Series {
  name: string;
  type: string;
  data: SeriesData[];
}

export interface PipelineResult {
  country : string,
  observedProperty : string,
  model: string;
  parameters: Record<string, ModelParameter>; 
  series: Series[];
  metrics: Metrics;
}

export interface Message {
  role : string,
  content : any
}