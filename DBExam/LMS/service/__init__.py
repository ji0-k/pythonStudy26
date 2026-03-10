from LMS.service.MemberService import MemberService
from LMS.service.BoardService import BoardService
from LMS.service.ScoreService import ScoreService

# 다른 패키지에서 import *로 처리 가능
__all__ = ['MemberService','BoardService', 'ScoreService']