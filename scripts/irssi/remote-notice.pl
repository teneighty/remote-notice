use strict;
use vars qw($VERSION %IRSSI);
use IO::Socket; 

use Irssi;
$VERSION = '0.0.1';
%IRSSI = (
	authors     => 'Tim Horton',
	contact     => 'tmhorton@gmail.com',
	name        => 'notify.pl',
	description => 'Send  notification to remote-notice server',
);

sub priv_msg {
	my ($server,$msg,$nick,$address,$target) = @_;
	write_json($nick, $msg);
}

sub hilight {
    my ($dest, $text, $stripped) = @_;
    if ($dest->{level} & MSGLEVEL_HILIGHT) {
        write_json($dest->{target}, $text );
    }
}

sub write_json {
	my ($title, $msg) = @_;
    my $sock = new IO::Socket::INET ( 
                    PeerAddr => 'localhost', 
                    PeerPort => '33333', 
                    Proto => 'tcp', 
                ); 
    return unless $sock; 
    print $sock "{\"title\" : \"$title\", \"msg\" : \"$msg\" }"; 
    close($sock);
}

Irssi::signal_add_last("message private", "priv_msg");
Irssi::signal_add_last("print text", "hilight");

