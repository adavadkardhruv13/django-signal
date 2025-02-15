import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# signal to show django signal is synchronous

@receiver(post_save, sender=User)
def sync_signal(sender, instance, **kwargs):
    print("\n[Synchronous] Signal handler started...")
    time.sleep(5)
    print("[Synchronous] Signal handler finished!")


# signal to show django signal  run in the same thread as the caller

@receiver(post_save, sender=User)
def signal_thread(sender, instance, **kwargs):
    print(f"[SIGNAL] Running in thread: {threading.get_ident()}")
    

# signal to show django signal  run in the same database transaction as the caller
    
@receiver(post_save, sender=User)
def signal_transaction_test(sender, instance, **kwargs):
    print("[SIGNAL] Signal executed!")
    raise Exception("[SIGNAL] Forcing a rollback!") 