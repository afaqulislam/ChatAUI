export default function DottedLoader() {
    return (
        <div className="flex items-center gap-1 py-3">
            <style>
                {`
          .dot {
            width: 0.5rem;
            height: 0.5rem;
            border-radius: 9999px;
            background: hsl(var(--primary));
            animation: wave 1.2s infinite ease-in-out;
          }

          .dot-1 { animation-delay: 0s; }
          .dot-2 { animation-delay: 0.1s; }
          .dot-3 { animation-delay: 0.2s; }
          .dot-4 { animation-delay: 0.3s; }

          @keyframes wave {
            0%, 60%, 100% {
              transform: translateY(0);
              opacity: 0.5;
            }
            30% {
              transform: translateY(-6px);
              opacity: 1;
            }
          }
        `}
            </style>

            <span className="dot dot-1" />
            <span className="dot dot-2" />
            <span className="dot dot-3" />
            <span className="dot dot-4" />
        </div>
    )
}
