const fs = require('fs')

function scanForSections(readmeContent) {
    const sectionMatcher = /<\!-- [A-Z_]+:START -->/g
    const matches = readmeContent.match(sectionMatcher)
    return matches.map(sectionTag => sectionTag.replace(/(<!--)|(-->)|(:START)/g, '').trim())
}

function getSectionBlock(readmeContent, sectionIdentifier) {
    if (!readmeContent) return ''
    const targetStart = `<!-- ${sectionIdentifier}:START -->`
    const targetStop = `<!-- ${sectionIdentifier}:END -->`
    const startIndex = readmeContent.indexOf(targetStart)
    const endIndex = readmeContent.indexOf(targetStop)
    const selectedBlock = readmeContent.slice(startIndex+targetStart.length, endIndex)
    return selectedBlock
}

function writeToMarkdown(section, content) {
    const formattedContent = `
    ---
    title: ${section}
    ---

    ${content}
    `

    fs.writeFileSync(`../docs/${section}.md`, formattedContent)
}

function parseReadme() {
    try {
        const readme = fs.readFileSync('../README.md', { encoding: 'utf8' })
        
        const sections = scanForSections(readme)
        const parsedSections = sections.map(section => {
            return {
                section,
                content: getSectionBlock(readme, section)
            }
        })

        parsedSections.forEach(({ section, content }) => {
            writeToMarkdown(section, content)
        })
    } catch(e) {
        console.error(e)
    }
}

parseReadme()
