function styleRecords()
{
    const table = document.getElementById("ranking-table")
    if (!table)
    {
        return;
    }
    const cells = table.querySelectorAll("td");
    cells.forEach(cell => 
    {
        if (cell.classList.contains("record"))
        {
            const text = cell.textContent
            const p1Record = text.slice(0, text.indexOf('-'))
            const p2Record = text.slice(text.indexOf('-') + 1, text.length)
            if (p1Record > p2Record)
            {
                const diff = p1Record - p2Record
                let red = 160
                let green = 255
                let blue = 160
                for (let i = diff; i > 0; i--)
                {
                    if (red > 0 && blue > 0)
                    {
                        red -= 40
                        blue -= 40
                    }
                }
                cell.style.backgroundColor=`rgb(${red}, ${green}, ${blue})`
            }
            else if (p1Record == p2Record)
            {
                cell.style.backgroundColor='yellow'
            }
            else
            {
                const diff = p2Record - p1Record
                let red = 255
                let green = 160
                let blue = 160
                for (let i = diff; i > 0; i--)
                {
                    if (green > 0 && blue > 0)
                    {
                        green -= 40
                        blue -= 40
                    }
                }
                cell.style.backgroundColor=`rgb(${red}, ${green}, ${blue})`
            }
        }
    });
}

function styleActivePage()
{
    const navLinks = document.querySelectorAll("nav a");
    navLinks.forEach((link) => {
        const currentPath = window.location.pathname.slice("1");
        const hrefArray = link.href.split("/");
        const thisPath = hrefArray[hrefArray.length - 1];

        if (currentPath === thisPath) 
        {
            link.classList.add("active");
        }
    });
}

function styleElements()
{
    styleRecords();
    styleActivePage();
}