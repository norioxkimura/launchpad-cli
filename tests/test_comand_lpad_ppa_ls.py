
from click.testing import CliRunner
from launchpadcli import cli

def test_command_lpad_ppa_ls():
    runner = CliRunner()
    result = runner.invoke(cli.lpad, [ 'ppa', 'ls' ])
    assert result.exit_code == 0
    assert result.output.rstrip() == 'lpad ppa ls'

