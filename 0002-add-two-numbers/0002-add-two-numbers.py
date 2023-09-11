# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None): # 밸류가 0값일 경우 None 반환
        self.val = val
        self.next = next #다음 노드를 가리키는 포인터

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node를 사용하여 결과 리스트를 시작
        dummy = ListNode()
        # 현재 처리 중인 노드를 나타내는 포인터 current
        current = dummy
        # 올림 값(두자리 세자리 숫자)을 저장(초기 설정)
        carry = 0
            #l1, l2, carry 값 존재 시 계속 실행됨
        while l1 or l2 or carry:
            # l1,l2 노드 값이 None인 경우 0로 대체
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 두 값을 더하고 올림 값을 추가합니다.
            total = val1 + val2 + carry
            # '//'는 정수 반환 연산자
            carry = total // 10
            # '%'는 나머지 연산자
            sum_val = total % 10
            
            # 결과 연결 리스트에 새 노드를 추가
            current.next = ListNode(sum_val)
            current = current.next
            
            # l1과 l2를 다음 노드로 이동
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # dummy의 다음 노드부터가 실제 결과이므로 그것을 반환
        return dummy.next
