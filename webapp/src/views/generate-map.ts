import europe from './europe.svg'


const parser = new DOMParser();
const svgDocument = parser.parseFromString(europe, "image/svg+xml");

console.log(svgDocument)

const paths = svgDocument.querySelectorAll("path");
const countries = Array.from(paths).map((path) => ({
  path: path.getAttribute("d") ?? "", 
  country: path.getAttribute("name") ?? "",
  isoCode: path.getAttribute("id") ?? "", 
}));


export {countries}
