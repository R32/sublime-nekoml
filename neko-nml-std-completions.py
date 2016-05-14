import sublime, sublime_plugin

# generate uuid: press ctrl+` and type: import uuid;uuid.uuid4()

NML_STD = {
	"list": [
		("iter('a->void, 'a list):void", "iter(${1:func}, ${2:list})$0"),
		("mem('k, 'k list):bool", "mem(${1:key}, ${2:list})$0"),
		("map('a->'b, 'a list):'b list", "map(${1:func}, ${2:list})$0"),
		("fold('b->'a->'b, 'b, 'a list):'b", "fold(${1:func}, ${2:init} ,${3:list})$0"),
		("length('a list):int", "length(${1:list})$0"),
		("hd('a list):'a", "hd(${1:list})$0"),
		("tl('a list):'a list", "tl(${1:list})$0"),
		("iter2('a->'b->void, 'a list, 'b list):void\t throw", "iter2(${1:func}, ${2:list1}, ${3:list2})$0"),
		("split(('a,'b)list):('a list, 'b list)", "split(${1:tplist})$0"),
		("exists('k->bool, 'k list):bool", "exists(${1:func}, ${2:list})$0"),
		("assoc('k, ('k,'v) list):'v\t == throw Not_found", "assoc(${1:func}, ${2:tplist})$0"),
		("phys('k, ('k,'v) list):'v\t === throw Not_found", "phys(${1:func}, ${2:tplist})$0"),
		("find('k->bool,'k list):'k\t throw Not_found", "find(${1:func}, ${2:list})$0"),
		("rev('a list):'a list", "rev(${1:list})$0"),
		("append('a list, 'a list):'a list", "append(${1:src}, ${2:dst})$0"),
		("concat('a list list):'a list", "concat(${1:listlist})$0"),
		("chop(int, 'a list):'a list\t throw arg", "chop(${1:begin}, ${2:list})$0"),
		("all('a->bool, 'a list):bool", "all(${1:func}, ${2:list})$0"),
		("none('a->bool, 'a list):bool", "none(${1:func}, ${2:list})$0"),
		("nth('a list, int):'a:\t throw arg", "nth(${1:list}, ${2:pos})$0"),
		("filter('a->bool, 'a list):'a list", "filter(${1:func}, ${2:list})$0"),
		("array('a list):'a array", "array(${1:list})$0"),
		("sort('a->'a->bool,'a list):'a list", "sort(${1:comp}, ${2:list})$0"),
	],

	"args": [
		("parse(head, decl, def: string->'a):void", "parse(${1:head}, ${2:decl}, ${3:def})$0"),
		("help(head: string, decl:(string, 'a->argtype, string)):void", "help(${1:head}, ${2:decl})$0"),
		("argtype\t type variants", "argtype$0"),
		("Invalid\t exception", "Invalid$0"),
		("parse_args(args: string array, head, decl, def: string->'a):void", "parse_args(${1:args}, ${2:hd}, ${3:decl}, ${4:def})$0"),
	],

	"array": [
		("string('a array):string", "string(${1:arr})$0"),
		("length('a array):int", "length(${1:arr})$0"),
		("create():'a array", "create()$0"),
		("add(a: 'a array, x:'a):void", "add(${1:arr}, ${2:x})$0"),
		("get(a: 'a array, p:int):'a", "get(${1:arr}, ${2:pos})$0"),
		("set(a: 'a array, p:int, x:'a):void", "set(${1:arr}, ${2:pos}, ${3:x})$0"),
		("make(size: int, x: 'a):'a array", "make(${1:len}, ${2:init})$0"),
		("init(size: int, f: int -> 'a):'a array", "init(${1:len}, ${2:func})$0"),
		("iter(f: 'a -> void, a:'a array):void", "iter(${1:func}, ${2:arr})$0"),
		("iteri(f: int -> 'a -> void, a: 'a array):void", "iteri(${1:func}, ${2:arr})$0"),
		("map(f: 'a -> 'b, a: 'a array):'b array", "map(${1:func}, ${2:arr})$0"),
		("sort(f: 'a -> 'a -> int, a:'a array):void", "sort(${1:comp}, ${2:arr})$0"),
		("list(a:'a array):'a list", "list(${1:arr})$0"),
		("append(src: 'a -> array, dst:'a array):void", "append(${1:src}, ${2:dst})$0"),
		("sub(a: 'a array, p: int, l: int):'a array", "sub(${1:arr}, ${2:pos},${3:len})$0"),
		("blit(dst: 'a array, pdst:int, src: 'a array, psrc: int l: int):void", "blit(${1:dst}, ${2:pdst}, ${3:src}, ${4:psrc} ${5:len})$0"),
		("index(a:'a array, it: 'a):int", "index(${1:arr}, ${2:x})$0"),
	],

	"buffer": [
		("t\t type Buffer", "t$0"),
		("create(): Buffer", "create()$0"),
		("add(b: Buffer, x:'a):void", "add(${1:buff}, ${2:x})$0"),
		("reset(b: Buffer):void", "reset(${1:buff})$0"),
		("add_sub(b: Buffer, sub:string, pos:int, len:int):void", "add_sub(${1:buff}, ${2:str}, ${3:pos}, ${4:len})$0"),
		("add_char(b: Buffer, ch:char):void", "add_char(${1:buff}, ${2:ch})$0"),
		("string(b: Buffer):string", "string(${1:buff})$0"),
	],

	"hashtbl": [
		("t\t type Hashtbl", "t$0"),
		("iter(f: 'a -> 'b -> void, h: ('a, 'b) Hashtbl, k: 'a):void", "iter( ${1:f}, ${2:h})$0"),
		("hash(x: 'a):int", "hash(${1:x})$0"),
		("create():('a, 'b) Hashtbl", "create()$0"),
		("length(h:('a, 'b) Hashtbl):int", "length(${1:h})$0"),
		("find(h: ('a, 'b) Hashtbl, k: 'a):'b\t throw Not_found", "find(${1:h}, ${2:k})$0"),
		("exists(h: ('a, 'b) Hashtbl, k: 'a):bool", "exists(${1:h}, ${2:k})$0"),
		("add(h: ('a, 'b) Hashtbl, k: 'a, v: 'b):void", "add(${1:h}, ${2:k}, ${3:v})$0"),
		("remove(h: ('a, 'b) Hashtbl, k: 'a):void", "remove(${1:h}, ${2:k})$0"),
		("replace(h: ('a, 'b) Hashtbl, k: 'a, v: 'b):void", "replace(${1:h}, ${2:k}, ${3:v})$0"),
	],

	"io": [
		("file\t type abstract", "file$0"),
		("input\t type record", "input$0"),
		("output\t type record", "output$0"),
		("Overflow: string\t exception", "Overflow(\"${1:msg}\")$0"),
		("Eof\t exception", "Eof$0"),
		("Closed\t exception", "Closed$0"),
		("Blocked\t exception", "Blocked$0"),
		# RAW FILE API
		("file_open(path: string, mod: string): file", "file_open(${1:path}, \"${2:r}\")$0"),
		("file_contents(path: string): string", "file_contents(${1:path})$0"),
		("file_close(f: file): void", "file_close(${1:file})$0"),
		("file_read(f: file, s: string, pos: int, len:int): int", "file_read(${1:f}, ${2:str}, ${3:pos}, ${4:len})$0"),
		("file_read_char(f: file): char", "file_read_char(${1:f})$0"),
		("file_write(f: file, s: string, pos: int, len:int): int", "file_write(${1:f}, ${2:str}, ${3:pos}, ${4:len})$0"),
		("file_write_char(f: file, c: char): void", "file_write_char(${1:f}, ${2:c})$0"),
		("file_open(f: file): void", "file_open(${1:f})$0"),

		("file_input(f: file): input", "file_input(${1:f})$0"),
		("read_file(path:string, bin: bool): input", "read_file(${1:path}, ${2:false})$0"),
		("read_string(str: string): input", "read_string(${1:str})$0"),
		("file_output(f: file): output", "file_output(${1:f})$0"),
		("write_file(path:string, bin: bool): output", "write_file(${1:path}, ${2:false})$0"),
		("write_string(): (output, void -> string)", "write_string()$0"),

		("file_stdin: file\t variable", "file_stdin$0"),
		("file_stdout: file\t variable", "file_stdout$0"),
		("file_stderr: file\t variable", "file_stderr$0"),
		("stdin: input\t variable", "stdin$0"),
		("stdout: output\t variable", "stdout$0"),
		("stderr: file\t variable", "stderr$0"),

		# INPUT API
		("create_in(r: void->char, i: string -> int -> int -> int, c: void -> void): input", "create_in(${1:in_read}, ${2:in_input}, ${3:in_close})$0"),
		("read_char(i: input): char", "read_char(${1:in})$0"),
		("read_byte(): char", "read_byte(${1:in})$0"),
		("input(i: input, dst: string, dstp: pos, n: len): char", "input(${1:src}, ${2:dst}, ${3:dstp}, ${4:len})$0"),
		("read(i: input, len: int): string\t throw ...", "read(${1:in}, ${2:len})$0"),
		("read_buf(i: input, len: int): string\t throw ...", "read_buf(${1:in}, ${2:len})$0"),
		("read_all(i: input): string\t throw Eof", "read_all(${1:in})$0"),
		("read_line(i: input): string\t throw Exit", "read_line(${1:in})$0"),
		("read_i32(i: input): int", "read_i32(${1:in})$0"),
		("read_ui16(i: input): int", "read_ui16(${1:in})$0"),
		("read_ui24(i: input): int", "read_ui24(${1:in})$0"),
		("read_i16(i: input): int", "read_i16(${1:in})$0"),
		("close_in(i: input): int\t", "close_in(${1:in})$0"),

		# OUTPUT API
		("create_out(write: char->void, output: string -> int -> int -> int, flush: void -> void, close: void -> void): output"
				, "create_out(${1:out_write}, ${2:out_output}, ${3:out_flush}, ${4:out_close})$0"),
		("write_char(o: output, c: char): void", "write_char(${1:out}, ${2:c})$0"),
		("write_byte(o: output, x: int): void", "write_byte(${1:out}, ${2:x})$0"),
		("write_i8(o: output, x: int): void\tthrow arg", "write_i8(${1:out}, ${2:x})$0"),
		("output(o: out, src: string, sp: int, len: int): void\t throw arg", "output(${1:out}, ${2:src}, {3:sp}, ${4:len})$0"),
		("write(o: output, x: string): void\t throw Blocked", "write(${1:out}, ${2:s})$0"),
		("write_i32(o: output, x: int): void", "write_i32(${1:out}, ${2:x})$0"),
		("write_ui16(o: output, x: int): void\tthrow arg", "write_ui16(${1:out}, ${2:x})$0"),
		("write_i16(o: output, x: int): void\tthrow arg", "write_i16(${1:out}, ${2:x})$0"),
		("write_ui24(o: output, x: int): void\tthrow arg", "write_ui24(${1:out}, ${2:x})$0"),
		("flush(o: output): void\t", "flush(${1:out})$0"),
		("close_out(o: output): void\t throw Closed", "close_out(${1:out})$0"),
		("printf(o: output, fmt: 'a format, p:'a): void\tthrow arg", "printf(${1:out}, ${2:fmt})$0"),
	],

	"math": [
		("pi\t var", "pi$0"),
		("atan2(float, float): float\t", "atan2(${1:f1}, ${2:f2})$0"),
		("pow(float, float): float\t", "pow(${1:f1}, ${2:f2})$0"),
		("abs(float): float\t", "abs(${1:f})$0"),
		("iabs(int): int\t", "iabs(${1:i})$0"),
		("ceil(float): int\t", "ceil(${1:f})$0"),
		("floor(float): int\t", "floor(${1:f})$0"),
		("round(float): int\t", "round(${1:f})$0"),
		("fceil(float): float\t", "fceil(${1:f})$0"),
		("ffloor(float): float\t", "ffloor(${1:f})$0"),
		("fround(float): float\t", "fround(${1:f})$0"),
		("fint(float): int\t", "fint(${1:f})$0"),
		("sqrt(float): float\t", "sqrt(${1:f})$0"),
		("atan(float): float\t", "atan(${1:f})$0"),
		("cos(float): float\t", "cos(${1:f})$0"),
		("sin(float): float\t", "sin(${1:f})$0"),
		("tan(float): float\t", "tan(${1:f})$0"),
		("log(float): float\t", "log(${1:f})$0"),
		("exp(float): float\t", "exp(${1:f})$0"),
		("acos(float): float\t", "acos(${1:f})$0"),
		("asin(float): float\t", "asin(${1:f})$0"),
	],

	"string": [
		("make(size: int, c: char): string", "make(${1:len}, ${2:c})$0"),
		("create(size: int): string", "create(${1:len})$0"),
		("length(s: string): int", "length(${1:s})$0"),
		("get(s: string, p: int): char\t throw arg", "get(${1:s}, ${2:p})$0"),
		("set(s: string, p: int, c: char): void\t throw arg", "set(${1:s}, ${2:p}, ${3:c})$0"),
		("blit(dst: string, p: int, src: string, p2: int, len: int): void\t throw arg"
				, "blit(${1:dst}, ${2:p}, ${3:src}, ${4:p2}, ${5:len})$0"),
		("sub(s: string, p: int, len: n): string\t throw arg", "sub(${1:s}, ${2:p}, ${3:len})$0"),
		("find(s: string, p: int, pat: string): int\t throw Not_found", "find(${1:str}, ${2:p}, ${3:pat})$0"),
		("split(s: string, sub: string): string list", "split(${1:str}, ${2:sub})$0"),
		("concat(sep: string, sl: string list): string", "concat(${1:sep}, ${2:sl})$0"),
		("escape(s: string): string", "escape(${1:s})$0"),
		("unescape(c: string): string\t throw arg", "unescape(${1:s})$0"),
		("lowercase(s: string): string", "lowercase(${1:s})$0"),
		("uppercase(s: string): string", "uppercase(${1:s})$0"),
		("serialize(x: 'a): string", "serialize(${1:x})$0"),
		("unserialize(x: string): 'a", "unserialize(${1:s})$0"),
		("is_printable(c: char): bool", "is_printable(${1:c})$0"),
		("escape_char(c: char): string", "escape_char(${1:c})$0"),
	],

	"sys": [
		("version\t type {maj: int, min: min, build: int}", "version$0"),
		("without_extension(s: string): string", "without_extension(${1:s})$0"),
		("extension(s: string): string", "extension(${1:s})$0"),
		("without_dir(s: string): string", "without_dir(${1:s})$0"),
		("args(s: string): string array", "args()$0"),
		("exit(code: int): 'a", "exit(${1:0})$0"),
		("exists(path: string): bool", "exists(${1:path})$0"),
		("get_env(s: string): string option", "get_env(${1:key})$0"),
		("put_env(k: string, v: string): void", "put_env(${1:k}, ${2:v})$0"),
		("get_cwd(): string", "get_cwd()$0"),
		("set_cwd(s: string): void", "set_cwd(${1:path})$0"),
		("executable_path(): string", "executable_path()$0"),
		("is_directory(s: string): bool", "is_directory(${1:path})$0"),
		("read_directory(s: string): string list", "read_directory(${1:path})$0"),
	],

	"stack": [
		("stack_item\t | {CFunction; Module:String; Pos:(String, int)}", "stack_item$0"),
		("stack\t |  = stack_item array", "Stack.stack"),
		("print(): void", "print()$0"),
		("call(): stack", "call()$0"),
		("exc(): stack", "exc()$0"),
		("dump(ch: output, st: stack): void", "dump(${1:ch}, {2:stack})$0"),
	],

	"set": [
		("'a t\t type Set", "t$0"),
		("add(set: 'a Set, x: 'a): 'a Set", "add(${1:set}, ${2:x})$0"),
		("create(cmp: 'a-> 'a-> int): 'a Set", "create(${1:cmp})$0"),
		("empty(): 'a Set", "empty()$0"),
		("iter(f: 'a -> void, set: 'a Set): 'a Set", "iter(${1:func}, ${2:set})$0"),
		("is_empty(set: 'a Set): bool", "is_empty(${1:set})$0"),
		("exists(set: 'a Set, x: 'a): bool", "exists(${1:set}, ${2:x})$0"),
		("remove(set: 'a Set, x: 'a): 'a Set", "remove(${1:set}, ${2:x})$0"),
		("union(s1: 'a Set, s2: 'a Set): 'a Set\t throw assert", "union(${1:s1}, ${2: s2})$0"),
		("inter(s1: 'a Set, s2: 'a Set): 'a Set\t throw assert", "inter(${1:s1}, ${2: s2})$0"),
		("diff(s1: 'a Set, s2: 'a Set): 'a Set\t throw assert", "diff(${1:s1}, ${2: s2})$0"),
	],

	"xml": [
		("t\t type Xml", "t$0"),
		("Error\t exception", "Error(\"${1:err}\")$0"),
		("parse(s: string): Xml", "parse(${1:s})$0"),
		("is_node(x: Xml): bool", "is_node(${1:x})$0"),
		("is_pcdata(x: Xml): bool", "is_pcdata(${1:x})$0"),
		("is_cdata(x: Xml): bool", "is_cdata(${1:x})$0"),
		("firstNode(x: Xml): Xml", "firstNode(${1:x})$0"),
		("nodes(x: Xml): Xml list\tthrow arg", "nodes(${1:x})$0"),
		("node_name(x: Xml): string\tthrow arg", "node_name(${1:x})$0"),
		("node_text(x: Xml): string\tthrow arg", "node_text(${1:x})$0"),
		("attrib(x: Xml, name: string): string\tthrow arg", "attrib(${1:x}, ${2:name})$0"),
		("write(o: output ,x: Xml): void\t", "write(${1:output}, ${2:x})$0"),
		("to_string(x: Xml): string\tthrow arg", "to_string(${1:x})$0"),
	],

	"regexp" : [
		("t\t type Regexp", "t$0"),
		("build(s: string): Regexp", "build(${1:s})$0"),
		("find(r: Regexp, s: string, pos: int, len: int): bool", "find(${1:r}, ${2:s}, ${3:p}, ${4:len})$0"),
		("matched(r: Regexp, nth: int): string\t throw Neko_error", "matched(${1:r}, ${2:0})$0"),
		("matched_pos(r: Regexp, nth: int): (int, int)\t throw Neko_error", "matched_pos(${1:r}, ${2:0})$0"),
		("split(r: Regexp, s: string): string list", "split(${1:r}, ${2:s})$0"),
	],

	"map" : [
		("('k, 'v) t\t type Map", "t$0"),
		("iter(f: 'a->'v->void, m: ('k, 'v) Map): void", "iter(${1:f}, ${2:m})$0"),
		("map(f: 'v->'u, m: ('k, 'v) Map): ('k, 'u) Map", "map(${1:f}, ${2:m})$0"),
		("fold(f: 'u->'v->'u, m: ('k, 'v) Map, acc: 'u): 'u", "fold(${1:f}, ${2:m}, ${3:acc})$0"),
		("create(cmp: 'k-> 'k-> int): ('k, 'v) Map", "create(${1:cmp})$0"),
		("empty(): ('k, 'v) Map", "empty()$0"),
		("is_empty(m: ('k, 'v) Map): bool", "is_empty(${1:m})$0"),
		("add(m: ('k, 'v) Map, 'k, 'v): ('k, 'v) Map", "add(${1:m}, ${2:k}, ${3:v})$0"),
		("find(m: ('k, 'v) Map, 'k): 'v\t throw Not_found", "find(${1:m}, ${2:k})$0"),
		("exists(m: ('k, 'v) Map, 'k): bool", "exists(${1:m}, ${2:k})$0"),
		("remove(m: ('k, 'v) Map, 'k): ('k, 'v) Map", "remove(${1:m}, ${2:k})$0"),
	],

	"reflect": [
		("neko_object\t type abstract", "neko_object$0"),
		("neko_abstract\t type abstract", "neko_abstract$0"),
		("neko_function\t type abstract", "neko_function$0"),
		("neko_array\t type abstract", "neko_array$0"),
		("neko_loader\t type abstract", "neko_loader$0"),
		("module\t type abstract", "module$0"),
		("value\t type variants", "value$0"),
		("value(n: neko_value): value", "value(${1:n})$0"),
		("neko_value(v: value): neko_value", "neko_value(${1:v})$0"),
		("asize(a: neko_array): int", "asize(${1:a})$0"),
		("aget(a: neko_array, p: int): value", "aget(${1:a}, ${2:p})$0"),
		("aset(a: neko_array, p: int, v:value): void", "aset(${1:a}, ${2:p}, ${3:v})$0"),
		("module_read(fread : string -> int -> int -> int): module", "module_read(${1:f})$0"),
		("loader_path(): string list", "loader_path()$0"),
		("module_read_path(path: string array, name: string, loader: neko_loader ): module"
				, "module_read_path(${1:paths}, ${2:name}, ${3:loader})$0"),
		("module_name(m: module): string", "module_name(${1:m})$0"),
		("module_execute(m: module): value", "module_execute(${1:m})$0"),
		("module_exports(m: module): value", "module_exports(${1:m})$0"),
		("module_loader(m: module): value", "module_loader(${1:m})$0"),
		("module_globals_count(m: module): int", "module_globals_count(${1:m})$0"),
		("module_get_global(m: module, n:int): value", "module_get_global(${1:m}, ${2:n})$0"),
		("module_set_global(m: module, n:int, v:value): void", "module_set_global(${1:m}, ${2:n}, ${3:v})$0"),
		("module_code_size(m: module): int", "module_code_size(${1:m})$0"),
	],

	"zip":[
		("in\t type abstract", "in$0"),
		("out\t type abstract", "out$0"),
		("flush\t type variants", "flush$0"),
		("result\t type record", "result$0"),
		("init(): void", "init()$0"),
		("output(v: int): out", "output(${1:v})$0"),
		("output_bound(o: out, size: int): int", "output_bound(${1:out}, ${2:size})$0"),
		("output_end(o: out): void", "output_end(${1:out})$0"),
		("output_buffer(o: out, in: string, ipos: int, out: string, opos: int): {done: bool, read: int, write: int}",
				"output_buffer(${1:o}, ${2:in}, ${3:ipos}, ${4:out}, ${5:opos})$0"),
		("input_end(i: in): void", "input_end(${1:i})$0"),
		("output_set_flush_mode(o: out, f: flush): void", "output_set_flush_mode(${1:o}, ${2:flush})$0"),
		("input_set_flush_mode(i: in, f: flush): void", "input_set_flush_mode(${1:i}, ${2:flush})$0"),
		("compress(string, level: int): string\t throw Error(s)", "compress(${1:s}, ${2:lv})$0"),
		("uncompress(string): string", "uncompress(${1:s})$0"),
	],

	"net": [
		("socket\t type abstract", "socket$0"),
		("ip\t type = int32", "ip$0"),
		("socket_new(bool): socket", "socket_new(${1:b})$0"),
		("socket_close(socket): void", "socket_close(${1:sc})$0"),
		("socket_send_char(socket, char): void", "socket_send_char(${1:sc}, ${2: char})$0"),
		("socket_send(sc: socket, s: string, p: int, len: int): int", "socket_send(${1:sc}, ${2:s}, ${3:p}, ${4:len})$0"),
		("socket_recv(sc: socket, s: string, p: int, len: int): int", "socket_recv(${1:sc}, ${2:s}, ${3:p}, ${4:len})$0"),
		("socket_recv_char(socket): char", "socket_recv_char(${1:sc})$0"),
		("socket_write(socket, string): void", "socket_write(${1:sc}, ${2: s})$0"),
		("socket_read(socket): string", "socket_read(${1:sc})$0"),
		("socket_connect(sc: socket, addr: ip, port: int): void", "socket_connect(${1:sc}, ${2:addr}, ${3:p})$0"),
		("socket_listen(sc: socket, port: int): void", "socket_listen(${1:sc}, ${3:p})$0"),
		("socket_bind(sc: socket, addr: ip, port: int): void", "socket_bind(${1:sc}, ${2:addr}, ${3:p})$0"),
		("socket_accept(sc: socket): socket", "socket_accept(${1:sc})$0"),
		("socket_peer(socket): (ip, int)", "socket_peer(${1:sc})$0"),
		("socket_host(socket): (ip, int)", "socket_host(${1:sc})$0"),
		("socket_set_timeout(socket, ?sec: int): void", "socket_set_timeout(${1:sc}, ${2:sec})$0"),
		("host_resolve(string): ip", "host_resolve(${1:sc})$0"),
		("host_to_string(addr: ip): string", "host_to_string(${1:addr})$0"),
		("host_local(): string", "host_local()$0"),
		("url_encode(string): string", "url_encode(${1:s})$0"),
		("url_decode(string): string", "url_decode(${1:s})$0"),
		("socket_select(read: socket array, write: socket array, others: socket array, timeout: float option): (socket array, socket array, socket array)"
				, "socket_select(${1:read}, ${2:write}, ${3:other}, ${4:timeout})$0"),
		("socket_io(socket): (IO.input, IO.output)", "socket_io(${1:sc})$0"),
		("start_server(addr: ip, port: int, on_connect: socket -> 'a, on_data: 'a -> bool): void"
				, "start_server(${1:addr}, ${2:port}, ${3:on_connect}, ${4:on_data})$0"),
	],

	"lexEngine": [
		# Regexp Parsing
		("InvalidRegexp\t exception: string", "InvalidRegexp(${1:msg})$0"),
		("single(c: char): charset", "single(${1:c})$0"),
		("group(chars: (char, char)list): charset", "group(${1:chars})$0"),
		("invalid(s: string)\t throw InvalidRegexp(s)", "invalid(${1:s})$0"),
		("escaped(s: string, i: i ref): char\t throw invalid(s)", "escaped(${1:s}, ${2:ref})$0"),
		("plus(r: t): t", "plus(${1:r})$0"),
		("star(r: t): t", "star(${1:r})$0"),
		("opt(r: t): t", "opt(${1:r})$0"),
		("next(r1: t, r2: t): t", "next(${1:r1}, ${2:r2})$0"),
		("parse(s: string): t", "parse(${1:s})$0"),
		# type
		("t\t type LexEngine variants", "t$0"),
		("charset\t type: (int, int) list", "charset$0"),
		("node\t type: mutable record", "node$0"),
		("state\t type: node list", "state$0"),
		("tables\t type: (int array array , int array)", "tables$0"),
		# charset
		("max_code\t var = 255", "max_code$0"),
		("cempty\t var = []", "cempty$0"),
		("call\t var = [(0, 255)]", "call$0"),
		("is_empty(c: 'a list):bool", "is_empty(${1:c})$0"),
		("cunion(c1: charset, c2: charset):charset\t throw assert", "cunion(${1:c1}, ${2:c2})$0"),
		("ccomplement(c: charset):charset", "ccomplement(${1:c})$0"),
		("cinter(c1: charset, c2: charset):charset\t throw assert", "cinter(${1:c1}, ${2:c2})$0"),
		("cdiff(c1: charset, c2: charset):charset\t throw assert", "cdiff(${1:c1}, ${2:c2})$0"),
		# nodes
		("node(g: void -> int):node", "node(${1:g})$0"),
		("add_node(state: node list, node): node list", "add_node(${1:state}, ${2:node})$0"),
		("add_nodes(state: node list, nodes: node list): node list", "add_nodes(${1:state}, ${2:nodes})$0"),
		("nodes(nfa: t array):node array", "nodes(${1:nfa})$0"),
		# NFA -> DFA
		("transitions(state: node list): (charset array, state array)", "transitions(${1:state})$0"),
		("determinize(nfa: t array): ( (int, int array, bool array) array, (int, int, int) list array )", "determinize(${1:nfa})$0"),
		# DFA -> Tables
		("make_trans(trans: (int, int, int) list, tbl: int array ):int array", "make_trans(${1:trans}, ${2:tbl})$0"),
		("make_tables(dfa: ((int, int array, bool array)array, trans: (int, int, int)list array), trans: int array ): tables", "make_tables(${1:dfa}, ${2:trans})$0"),
	],

	"lexer": [
		("pos\t type record", "pos$0"),
		("cur\t type mutable record", "cur$0"),
		("'a t\t type mutable record", "t$0"),
		("('a,'b) tables\t type record", "tables$0"),
		("Invalid_rule\t exception: string", "Invalid_rule(${1:s})$0"),
		("null_pos\t var", "null_pos$0"),
		("source(p: pos): string", "source(${1:p})$0"),
		("line(p: pos): int", "line(${1:p})$0"),
		("punion(p1: pos, p2: pos): pos", "punion(${1:p1}, ${2:p2})$0"),
		("create(data: 'a): 'a t", "create(${1:data})$0"),
		("data(l: 'a t): 'a", "data(${1:l})$0"),
		("set(l: 'a t, data: 'a): 'a", "set(${1:l}, ${2:data})$0"),
		("input(l: 'a t, source: string, input: IO.input, line: int, pos: int): int", "input(${1:l}, ${2:s}, ${3:i}, ${4:n}, ${5:p})$0"),
		("curpos(l: 'a t): pos", "curpos(${1:l})$0"),
		("current(l: 'a t): string", "current(${1:l})$0"),
		("read(l: 'a t): char", "read(${1:l})$0"),
		("inc_line(l: 'a t, c: char): void", "inc_line(${1:l}, ${2:c})$0"),
		("char(l: 'a t): char option", "char(${1:l})$0"),
		("token(l: 'a t, t: tables): 'a\t throw ...", "token(${1:l}, ${2:t})$0"),
		("build(rules: (string, 'a t -> 'b) list, def: 'a t -> 'b): ('a,'b) tables\t throw ...", "build(${1:rules}, ${2:def})$0"),
		("empty(): ('a,'b) tables", "empty()$0"),
	]
}

# print(len(NML_STD) == 19)

class NmlProject(sublime_plugin.EventListener):

	empty = []

	def on_query_completions(self, view, prefix, locations):
		pt = locations[0] - 1;
		if(view.match_selector(pt, "support.function.dot")):
			ns = view.scope_name(pt)
			try:
				global NML_STD
				p1 = 4 + ns.index("std.", 10) # "source.nml std.xxxxx"
				key = ns[p1: ns.index(' ',p1 + 1)]
				if key in NML_STD:
					# sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS == 8 | 16 == 24
					return (NML_STD.get(key), 24)
			except:
				pass
		elif(view.match_selector(pt, "keyword.control.dot")):
			return(self.empty,24)







