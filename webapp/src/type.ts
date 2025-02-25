export interface Country { 
    country: string,
    isoAlpha2: string, 
    clicked: boolean 
}

export interface Option {
    name: string,
    isoAlpha2?: string, 
    code?: string,
}

export interface BarData {
    x: string,
    y: number,
}