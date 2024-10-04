from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from review.entity.review import Review
from review.serializers import ReviewSerializer
from review.service.review_service_impl import ReviewServiceImpl


# Create your views here.

class ReviewView(viewsets.ViewSet):
    queryset = Review.objects.all()

    reviewService = ReviewServiceImpl.getInstance()

    def list(self, request):
        reviewList = self.reviewService.list()
        serializer = ReviewSerializer(reviewList, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = request.data

            image = request.FILES.get('reviewImage')
            title = data.get('title')
            writer = data.get('writer')
            content = data.get('content')

            if not all([title, writer, content]):
                return Response({'error': '내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)
            if image:
                self.reviewService.createReview(title, writer, content, image)
            else:
                self.reviewService.createReviewWithoutImage(title, writer, content)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)