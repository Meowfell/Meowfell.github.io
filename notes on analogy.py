html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Notes on Analogy</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1 {
            font-size: 24px;
            color: #333;
        }
        p {
            margin-bottom: 10px;
        }
        .quote {
            margin-bottom: 20px;
        }
        .source {
            font-style: italic;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Notes on Analogy</h1>
    <div class="quote">
        <p>"The English word 'analogy' originates from the Greek <i>analogia</i>, meaning mathematical proportion (such as 2:4::4:8)."</p>
    </div>
    <div class="quote">
        <p>"The topic of analogy has a special place in the field of cognitive science. Modern cognitive science arose as a discipline in the final half-century of the millennium just ended—scarcely a tick on the clock of human life on earth. Although several converging factors led to the development of cognitive science, perhaps the most critical was an analogy—that between human information processing and the processing performed by the digital computer. This basic analogical insight, that cognition can be systematically analyzed as a form of computation, guided early work on such cognitive processes as memory, attention, perception, and problem-solving.</p>
        <p>Although an analogy provided a major part of the foundation of cognitive science at its inception, the study of analogy itself as a cognitive process did not receive much attention until somewhat later. Modern views of analogy can be traced to such pioneering influences as the philosopher Mary Hesse (1966), whose treatise on analogy in science argued that analogies are powerful forces in discovery and conceptual change. For some time, however, most research on analogy, both in artificial intelligence (Evans 1968) and in psychology (Piaget, Montangero, and Billeter 1977; Sternberg 1977) focused on four-term analogy problems of the sort used in intelligence tests (e.g., cat is to kitten as dog is to what?), rather than on the richer analogies used in science and everyday life.</p>
        <p>About 1980, several research projects in artificial intelligence and psychology began to take a broader view of analogy. Researchers in artificial intelligence started to grapple with the use of complex analogies in reasoning and learning (Winston 1980; Schank 1982; Carbonell 1983, 1986; Hofstadter 1984). This exploration led to a more general focus on the role of experience in reasoning and the relationships among reasoning, learning, and memory, giving rise to an approach termed "case-based" reasoning (e.g., Kolodner 1993)."</p>
        <p class="source">- Analogy in Cognitive Science</p>
    </div>
    <div class="quote">
        <p>"Cognitive theories realized that metaphor is not an exceptional decorative occurrence in language, but is a main mechanism by which humans understand abstract concepts and carry out abstract reasoning (e.g., Lakoff and Johnson [22], Lakoff [21], Johnson [18]). On this view, metaphors are structure-preserving mappings (partial homomorphisms) between conceptual domains, rather than linguistic constructions."</p>
        <p class="source">- Computation for Metaphors, Analogy and Agents, page 3</p>
    </div>
    <div class="quote">
        <p>"In sum, similarity plays a key role in many of the best-known theories of concepts, and it does so in two interrelated ways: (a) Similarity determines the typicality of an instance with respect to a category; and (b) similarity determines the probability that people will classify an instance as a category member. One way to put these ideas together is to assume first that similarity accounts for typicality; that is, typicality just is either similarity of an instance to a prototype or average similarity of the instance to known category members."</p>
        <p class="source">- Similarity and Analogical Reasoning, page 27</p>
    </div>
    <div class="quote">
        <p>"Analogy pervades all our thinking, our everyday speech and our trivial conclusions as well as artistic ways of expression and the highest scientific achievements."</p>
        <p class="source">- Polya, How To Solve It, page 37</p>
    </div>
</body>
</html>"""

# Write the HTML content to a file
with open("notes_on_analogy.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
