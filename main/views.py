from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

from .models import Video


# ============================================================
# HOME
# ============================================================

def home(request):

    featured_video = Video.objects.filter(
        featured=True
    ).first()

    # If no featured video exists in the database,
    # automatically use the portfolio video.
    if not featured_video:

        featured_video = Video(
            title="My Showreel",
            category="cinematic",
            description="My latest video editing showreel.",
            video="videos/Portfolio.mp4",
            featured=True,
        )

    return render(
        request,
        "home.html",
        {
            "featured_video": featured_video,
        }
    )


# ============================================================
# WORK
# ============================================================

def work(request):

    videos = Video.objects.all().order_by("-created_at")

    return render(
        request,
        "work.html",
        {
            "videos": videos,
        }
    )


# ============================================================
# SERVICES
# ============================================================

def services(request):

    return render(
        request,
        "services.html"
    )


# ============================================================
# ABOUT
# ============================================================

def about(request):

    return render(
        request,
        "about.html"
    )


# ============================================================
# CONTACT
# ============================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        project_type = request.POST.get("project_type", "").strip()
        budget = request.POST.get("budget", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not project_type or not budget or not message:

            messages.error(
                request,
                "Please fill in all the required fields."
            )

            return redirect("contact")

        subject = f"New Portfolio Enquiry from {name}"

        email_message = f"""
NEW PROJECT ENQUIRY
===================

CLIENT DETAILS

Name:
{name}

Email:
{email}

Project Type:
{project_type}

Estimated Budget:
{budget}


PROJECT DETAILS
===============

{message}


===================

This enquiry was submitted through
Manikanta's video editing portfolio.
"""

        try:

            email = EmailMessage(
                subject=subject,
                body=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )

            email.send(
                fail_silently=False
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:

            print("EMAIL ERROR:", e)

            messages.error(
                request,
                "Sorry, something went wrong while sending your message. Please try again."
            )

        return redirect("contact")

    return render(
        request,
        "contact.html"
    )