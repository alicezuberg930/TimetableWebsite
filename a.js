// import * as puppeteer from "puppeteer"
const puppeteer = require("puppeteer")
async function ScrapeTimetable() {
    const browser = await puppeteer.launch({ headless: false })
    const page = await browser.newPage()
    await page.goto("http://thongtindaotao.sgu.edu.vn/Default.aspx?page=thoikhoabieu&sta=1&id=3119410401")
    const headings = await page.$$('.body-table')
    for (let i = 0; i < headings.length; i++) {
        let element = headings[i]
        let headingtext = await page.evaluate(element => element.textContent, element)
        console.log(headingtext)
        console.log("\n")
    }
    await browser.close()
}
ScrapeTimetable()