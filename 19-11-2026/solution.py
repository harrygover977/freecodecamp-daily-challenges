def convert(heading: str) -> str:
    """Converts a Markdown heading to a HTML heading."""
    invalid_str = "Invalid format"
    stripped_heading = heading.strip()
    hash_stripped_heading = stripped_heading.strip("#").strip()
    heading_beginning = stripped_heading.split()[0]
    num_hashes = heading_beginning.count("#")
    
    if num_hashes > 6 or num_hashes != len(heading_beginning):
        return invalid_str
    else:
        heading = f"<h{num_hashes}>{hash_stripped_heading}</h{num_hashes}>"
    return heading
        
assert convert("# My level 1 heading") == "<h1>My level 1 heading</h1>"
assert convert("My heading") == "Invalid format"
assert convert("##### My level 5 heading") == "<h5>My level 5 heading</h5>"
assert convert("#My heading") == "Invalid format"
assert convert("  ### My level 3 heading") == "<h3>My level 3 heading</h3>"
assert convert("####### My level 7 heading") == "Invalid format"
assert convert("## My #2 heading") == "<h2>My #2 heading</h2>"
