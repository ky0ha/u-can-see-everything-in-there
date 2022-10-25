# def greeting(name: str) -> str: return 'hello'+name
@accepts(str) def greeting(name): return 'hello' + name
greeting(12)