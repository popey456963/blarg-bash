{"filter":false,"title":"ruby.rb","tooltip":"/ruby.rb","undoManager":{"mark":3,"position":3,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":59,"column":3},"action":"insert","lines":["class MarkdownTableFormatter","","  def initialize(string, header=true)","    @doc = string","    @header = header","  end","","  # converts the markdown string into an array of arrays","  def parse","    @table = []","    rows = @doc.split /\\r?\\n/","    rows.each do |row|","      row_array = row.split(\"|\")","      row_array.each { |cell| cell.strip! }","      @table.push row_array","    end","    @table.delete_at(1) if @header #strip header separator","    @table","  end","","  def table","    @table ||= parse","  end","","  def column_width(column)","    width = 0","    table.each do |row|","      length = row[column].strip.length","      width = length if length > width","    end","    width","  end","","  def pad(string,length)","    string.strip.ljust(length, ' ')","  end","","  def separator(length)","    \"\".ljust(length,'-')","  end","","  def header_separator_row","    output = []","    [*0...table.first.length].each do |column|","      output.push separator(column_width(column))","    end","    output","  end","","  def to_md","    output = \"\"","    t = table.clone","    t.insert(1, header_separator_row) if @header","    t.each_with_index do |row, index|","      row.map!.with_index { |cell, index| cell = pad(cell, column_width(index)) }","      output += \"#{row.join(\" | \").lstrip} |\\n\"","    end","    output","  end","end"]}]}],[{"group":"doc","deltas":[{"start":{"row":53,"column":30},"end":{"row":53,"column":31},"action":"insert","lines":["!"]}]}],[{"group":"doc","deltas":[{"start":{"row":53,"column":31},"end":{"row":53,"column":32},"action":"insert","lines":["!"]}]}],[{"group":"doc","deltas":[{"start":{"row":53,"column":32},"end":{"row":53,"column":33},"action":"insert","lines":["!"]}]}]]},"ace":{"folds":[],"scrolltop":791,"scrollleft":0,"selection":{"start":{"row":53,"column":33},"end":{"row":53,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":36,"mode":"ace/mode/text"}},"timestamp":1421924793000,"hash":"1697b2937b99675203a119ecd14d6188083e48c9"}